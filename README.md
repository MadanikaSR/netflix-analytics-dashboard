# Netflix Data Analytics Project

## Problem Statement
The OTT (Over-The-Top) streaming industry is highly competitive. Understanding content strategy, regional focus, and genre popularity is crucial for business growth. This project analyzes a public Netflix dataset to deliver actionable business insights through a clean, professional Power BI dashboard, supported by a robust data pipeline using Python and SQL.

## Architecture
This project utilizes a modern analytics stack:
1. **Python (Pandas, NumPy):** Used for robust data extraction, cleaning, and feature engineering.
2. **SQL (SQLite):** Used as the core analytical database to validate metrics, aggregate data efficiently, and serve verified tables for reporting.
3. **Power BI:** The visualization layer, consuming the cleaned dataset to produce a highly interactive, Netflix-themed dashboard.

## Folder Structure
- `data/` - Raw datasets (e.g., `netflix_titles.csv`)
- `src/` - Python scripts for cleaning and feature engineering
- `outputs/` - Cleaned CSVs and SQLite databases
- `sql/` - SQL queries for generating key business insights
- `dashboard/` - Power BI dashboard documentation and UI guides
- `notebooks/` - (Optional) Jupyter notebooks for exploratory data analysis

## Steps to Run the Project
1. **Prerequisites:** Ensure you have Python installed.
2. **Install Libraries:** Run `pip install -r requirements.txt`.
3. **Download Data:** Ensure `data/netflix_titles.csv` is populated. A standard Kaggle Netflix dataset was used.
4. **Data Pipeline:** 
   - Run `python src/data_cleaning.py` to clean missing values, split categories, and normalize dates.
   - Run `python src/feature_engineering.py` to extract duration features.
5. **SQL Layer:**
   - Run `python sql/load_data.py` to import the cleaned data into a SQLite database (`outputs/netflix.db`).
   - Execute queries defined in `sql/queries.sql` to generate insights.
6. **Dashboard:**
   - Open Power BI and follow instructions in `dashboard/dashboard_instructions.md` to recreate the dashboard.

## Key Insights Generated
- **Growth Trends:** A massive exponential increase in content addition post-2015, signaling a shift towards aggressive global expansion.
- **Regional Dominance:** While the United States leads content production, India and the UK represent massive secondary markets.
- **Format Strategy:** Movies typically outnumber TV Shows, but TV Show production has accelerated as serial content proves to have highly retentive qualities for subscriptions.
- **Genre Popularity:** International Movies, Dramas, and Comedies remain the top-tier categories globally.

## Dashboard
*(Placeholder for Dashboard Screenshot)*  
![Netflix Dashboard](placeholder_image_link_here)
