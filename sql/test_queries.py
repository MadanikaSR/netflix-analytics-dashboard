import sqlite3
import pandas as pd
import os
import sys

def test_database(db_path, sql_path):
    print("==================================================")
    print("🎬 NETFLIX ANALYTICS : SQL MODULE TESTING")
    print("==================================================")
    
    # 1. Error Handling: Missing DB File
    if not os.path.exists(db_path):
        print(f"❌ ERROR: Database file not found at '{db_path}'.")
        print("Please run 'python sql/load_data.py' first.")
        sys.exit(1)
        
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 2. Error Handling: Missing Table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='netflix_titles';")
        if not cursor.fetchone():
            print("❌ ERROR: Table 'netflix_titles' does not exist in the database.")
            sys.exit(1)
            
        print("✅ Database Connection: SUCCESS")
        print("✅ Table 'netflix_titles': VERIFIED\n")
        
        # 3. Total Row Count Validation
        cursor.execute("SELECT COUNT(*) FROM netflix_titles;")
        total_records = cursor.fetchone()[0]
        print(f"📊 Total Records in Database: {total_records:,}")
        if total_records == 0:
            print("⚠️ WARNING: The table is empty.")
            sys.exit(1)
        print("-" * 50)
            
        # 4. Error Handling: Missing SQL File
        if not os.path.exists(sql_path):
            print(f"❌ ERROR: SQL file not found at '{sql_path}'.")
            sys.exit(1)
            
        # 5. Execute Queries from sql/queries.sql
        print("\n🚀 EXECUTING QUERIES FROM 'sql/queries.sql'...\n")
        with open(sql_path, "r", encoding="utf-8") as f:
            sql_script = f.read()
            
        # Split by semicolon to get individual queries
        queries = [q.strip() for q in sql_script.split(';') if q.strip()]
        
        for i, query in enumerate(queries, 1):
            try:
                # Extract first line as description if it's a comment
                lines = query.strip().split('\n')
                
                # Combine consecutive comments to form the full description
                comments = [line.replace('--', '').strip() for line in lines if line.strip().startswith('--')]
                description = " ".join(comments) if comments else f"Query {i} Execution"
                
                print(f"▶️  TEST {i}: {description}")
                df = pd.read_sql_query(query, conn)
                
                if df.empty:
                    print("   [No Results Returned]")
                else:
                    # Print using pandas to_string for neat tabular format
                    print(df.to_string(index=False))
                print("-" * 50)
                
            except sqlite3.Error as e:
                print(f"❌ SQL ERROR in Query {i}: {e}")
                print(f"Query text:\n{query}")
                print("-" * 50)
                
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("🔒 Database Connection Closed.")
            print("==================================================")

if __name__ == "__main__":
    DB_FILE = os.path.join("outputs", "netflix.db")
    SQL_FILE = os.path.join("sql", "queries.sql")
    test_database(DB_FILE, SQL_FILE)
