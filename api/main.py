from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="Medical Data API")

DB_CONFIG = {
    "dbname": "medical_db",
    "user": "postgres",
    "password": "password123",
    "host": "localhost",
    "port": "5432"
}

@app.get("/")
def home():
    return {"status": "Online", "message": "Medical Warehouse API is running"}

@app.get("/messages")
def get_messages():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        # Joining messages with our new detections from Task 3
        cur.execute("""
            SELECT m.channel_name, m.message_text, d.label, d.confidence
            FROM raw.telegram_messages m
            LEFT JOIN raw.detections d ON m.channel_name = d.channel_name
            LIMIT 20;
        """)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except Exception as e:
        return {"error": str(e)}