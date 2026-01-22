import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Replace 'yourpassword' with your actual DB password
DB_URL = "postgresql://postgres:yourpassword@localhost:5432/medical_db"
engine = create_engine(DB_URL)

try:
    count = pd.read_sql("SELECT count(*) FROM raw.telegram_messages", engine)
    print("--- Database Verification ---")
    print(f"Total rows in raw.telegram_messages: {count.iloc[0,0]}")
    
    # Show a sample of the data
    sample = pd.read_sql("SELECT channel_name, message_date, views FROM raw.telegram_messages LIMIT 5", engine)
    print("\nData Sample:")
    print(sample)
except Exception as e:
    print(f"Error: Could not connect or query database. {e}")