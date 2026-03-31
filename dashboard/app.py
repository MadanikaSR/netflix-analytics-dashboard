import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("outputs/cleaned_data.csv")

df = load_data()

# ---------------- CSS ----------------
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(180deg, #0B0F19 0%, #111827 100%);
    color: #E5E7EB;
}

/* REMOVE PADDING */
.block-container {
    padding: 2rem;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #0A0F1C;
    border-right: 1px solid #1F2937;
}

/* SIDEBAR TITLE */
section[data-testid="stSidebar"] h1 {
    color: #E5E7EB;
    font-size: 20px;
}

/* LABELS */
section[data-testid="stSidebar"] label {
    color: #9CA3AF !important;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* DROPDOWNS */
section[data-testid="stSidebar"] .stSelectbox div {
    background-color: #111827 !important;
    color: #E5E7EB !important;
    border-radius: 8px;
    border: 1px solid #1F2937;
}

/* DROPDOWN TEXT */
section[data-testid="stSidebar"] .stSelectbox span {
    color: #E5E7EB !important;
}

/* HOVER */
section[data-testid="stSidebar"] .stSelectbox div:hover {
    border: 1px solid #6366F1;
}

/* CARDS */
.card {
    background: linear-gradient(145deg, #111827, #0f172a);
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #1F2937;
    transition: all 0.3s ease;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 10px 25px rgba(99, 102, 241, 0.2);
}

.card-title {
    font-size: 12px;
    color: #9CA3AF;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.card-value {
    font-size: 30px;
    font-weight: 700;
    margin-top: 5px;
}

/* SECTION TITLES */
.section-title {
    font-size: 20px;
    font-weight: 600;
    margin: 15px 0;
    color: #E5E7EB;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("# 🎬 Netflix Dashboard")
st.sidebar.markdown("### Filters")

type_filter = st.sidebar.selectbox(
    "Content Type",
    ["All"] + list(df["type"].dropna().unique())
)

year_filter = st.sidebar.selectbox(
    "Year Added",
    ["All"] + sorted(df["year_added"].dropna().unique())
)

country_filter = st.sidebar.selectbox(
    "Country",
    ["All"] + sorted(df["country"].dropna().unique())
)

st.sidebar.markdown("---")
st.sidebar.caption("Netflix Titles Dataset")

# ---------------- FILTER DATA ----------------
filtered_df = df.copy()

if type_filter != "All":
    filtered_df = filtered_df[filtered_df["type"] == type_filter]

if year_filter != "All":
    filtered_df = filtered_df[filtered_df["year_added"] == year_filter]

if country_filter != "All":
    filtered_df = filtered_df[filtered_df["country"] == country_filter]

# ---------------- KPIs ----------------
total_titles = len(filtered_df)
movies = len(filtered_df[filtered_df["type"] == "Movie"])
tv_shows = len(filtered_df[filtered_df["type"] == "TV Show"])

# ---------------- HEADER ----------------
st.title("📊 Content Intelligence")
st.caption("Tracking Netflix content trends, regional distribution, and genre insights")

# ---------------- KPI CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Total Titles</div>
        <div class="card-value">{total_titles}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Movies</div>
        <div class="card-value">{movies}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">TV Shows</div>
        <div class="card-value">{tv_shows}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CHARTS ----------------
col1, col2 = st.columns(2)

# Growth Chart
with col1:
    st.markdown('<div class="section-title">Content Growth</div>', unsafe_allow_html=True)

    growth = filtered_df.groupby("year_added").size().reset_index(name="count")

    fig1 = px.line(growth, x="year_added", y="count")
    fig1.update_traces(line_shape="spline", line=dict(width=3))

    fig1.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=30, b=10),
    )

    st.plotly_chart(fig1, use_container_width=True)

# Pie Chart
with col2:
    st.markdown('<div class="section-title">Movies vs TV Shows</div>', unsafe_allow_html=True)

    pie = filtered_df["type"].value_counts().reset_index()
    pie.columns = ["type", "count"]

    fig2 = px.pie(pie, values="count", names="type", hole=0.6)

    fig2.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------- COUNTRY ----------------
st.markdown('<div class="section-title">Top Countries</div>', unsafe_allow_html=True)

country = filtered_df["country"].value_counts().head(10).reset_index()
country.columns = ["country", "count"]

fig3 = px.bar(country, x="count", y="country", orientation="h")

fig3.update_layout(
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- GENRE ----------------
st.markdown('<div class="section-title">Genre Distribution</div>', unsafe_allow_html=True)

genre = filtered_df["listed_in"].value_counts().head(10).reset_index()
genre.columns = ["genre", "count"]

fig4 = px.bar(genre, x="count", y="genre", orientation="h")

fig4.update_layout(
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)

st.plotly_chart(fig4, use_container_width=True)