import os
import json
import pandas as pd
from sqlalchemy import create_engine

# Database Connection
engine = create_engine('postgresql://postgres:password123@localhost:5432/medical_db')

def load_data():
    # Adjust this path if your JSONs are stored elsewhere
    base_path = "data" 
    all_data = []
    
    print("Searching for JSON files...")
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    # Handle both single objects and lists of objects
                    if isinstance(content, list):
                        all_data.extend(content)
                    else:
                        all_data.append(content)
    
    if all_data:
        df = pd.DataFrame(all_data)
        # We use 'replace' to ensure a fresh start
        df.to_sql('telegram_messages', engine, schema='raw', if_exists='replace', index=False)
        print(f"✅ Success! Loaded {len(df)} rows into raw.telegram_messages")
    else:
        print("❌ Error: No JSON data found in the 'data' folder.")

if __name__ == "__main__":
    load_data()
