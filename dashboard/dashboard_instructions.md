# Power BI Dashboard Instructions

This document provides a step-by-step guide to building the professional Netflix Analytics Dashboard using Power BI.

## 1. Connect Data
1. Open Power BI Desktop.
2. Click on **Get Data** -> **Text/CSV**.
3. Navigate to `outputs/cleaned_data.csv` and load the data.

## 2. Define KPIs (Cards)
At the top of your dashboard, create four **Card** visualizations for the following metrics:
- **Total Titles:** Count of `show_id`.
- **Total Movies:** Count of rows where `type` = 'Movie'.
- **Total TV Shows:** Count of rows where `type` = 'TV Show'.
- **Top Genre:** The mode (most frequent) of `primary_genre`.

## 3. Creating the Charts
Create the following visualizations to capture the required business insights:

- **Line Chart (Content Growth Over Time):**
  - **X-axis:** `year_added`
  - **Y-axis:** Count of `show_id`
  - *Insight:* Shows the trend of how Netflix has grown its content library year by year.

- **Bar Chart (Top 10 Countries by Content):**
  - **Y-axis:** `primary_country`
  - **X-axis:** Count of `show_id`
  - *Filter:* Exclude 'Unknown' countries.
  - *Insight:* Highlights regional dominance in content production.

- **Donut Chart (Movies vs TV Shows):**
  - **Legend:** `type`
  - **Values:** Count of `show_id`
  - *Insight:* Shows the ratio of Movies to TV Shows on the platform.

- **Column Chart (Genre Distribution):**
  - **X-axis:** `primary_genre`
  - **Y-axis:** Count of `show_id`
  - *Filter:* Top 5 or Top 10 genres.
  - *Insight:* Highlights consumer preference and platform focus on genres like Dramas, Comedies, and Documentaries.

## 4. Add Slicers / Filters
On the left or right panel, add slicers for deep dives:
- **Year Slicer:** Filter using `year_added` (List or Range).
- **Country Slicer:** Filter using `primary_country` (Dropdown).
- **Type Slicer:** Movie vs TV Show.

## 5. UI / UX Design Guidelines
To ensure a professional and premium look:
- **Background Color:** Use a dark theme (e.g., `#141414` background with white text, adhering to Netflix's UI) or a very clean, minimalist light theme (e.g., `#F8F9FA`).
- **Accent Color:** Use Netflix Red (`#E50914`) for primary data points or highlights.
- **Font Selection:** Set default font to *Segoe UI* or *DIN* throughout the dashboard.
- **Spacing:** Ensure equal margins and paddings around all charts. Do not clutter. 
- **Borders:** Add a subtle rounded border and a very light shadow to visualization cards for a card-like UI effect.

## 6. Business Insights
- **Growth Trends:** Look at the Line Chart to see when Netflix started massively scaling its original content.
- **Regional Focus:** Utilize the Country Bar Chart to determine which non-US regions serve as secondary markets (e.g., India, UK).
- **Format Shift:** Note the composition of Movies vs TV Shows, which can indicate content formatting strategies over time.
