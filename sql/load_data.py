import sqlite3
import pandas as pd
import os

def load_data_to_sqlite(csv_path, db_path):
    print(f"Loading cleaned data from {csv_path}...")
    df = pd.read_csv(csv_path)
    
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    
    table_name = "netflix_titles"
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    
    print(f"Data successfully loaded into {db_path} table '{table_name}'.")
    
    # Verify row count
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"Total records in '{table_name}': {count}")
    
    conn.close()

if __name__ == "__main__":
    load_data_to_sqlite(
        os.path.join("outputs", "cleaned_data.csv"),
        os.path.join("outputs", "netflix.db")
    )
