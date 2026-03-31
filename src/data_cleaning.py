import pandas as pd
import numpy as np
import os

def clean_data(input_path, output_path):
    print(f"Loading data from {input_path}...")
    df = pd.read_csv(input_path)
    
    # 1. Handle missing values
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    
    # Drop rows where 'date_added' or 'rating' is missing
    df = df.dropna(subset=['date_added', 'rating']).copy()
    
    df['country'] = df['country'].fillna('Unknown')
    
    # 2. Convert date_added to datetime
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df = df.dropna(subset=['date_added']).copy()  # drop any unparseable dates
    
    # 3. Extract year_added, month_added
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    
    # 4. Clean country column (split multiple countries, keep the first one as primary)
    df['primary_country'] = df['country'].apply(lambda x: str(x).split(',')[0].strip())
    
    # 5. Normalize genre/category (split multiple and keep primary)
    df['primary_genre'] = df['listed_in'].apply(lambda x: str(x).split(',')[0].strip())
    
    # 6. Remove duplicates
    df = df.drop_duplicates()
    
    # Save cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}. Total rows: {len(df)}")

if __name__ == "__main__":
    input_csv = os.path.join("data", "netflix_titles.csv")
    output_csv = os.path.join("outputs", "cleaned_data.csv")
    clean_data(input_csv, output_csv)
