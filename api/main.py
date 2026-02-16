from fastapi import FastAPI
import pandas as pd
from datetime import datetime, timedelta

app = FastAPI(title="Medical Warehouse API - Demo Mode")

@app.get("/")
def read_root():
    return {"message": "API Running in Demo Mode", "status": "Database Offline - Using Mock Data"}

@app.get("/analytics/summary")
def get_summary():
    return {
        "total_messages_processed": 1420,
        "average_sentiment": 0.68,
        "top_channel": "DoctorsHub_Eth",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/analytics/trends")
def get_trends():
    # Generates 7 days of fake data for your charts
    today = datetime.now()
    return [
        {"date": (today - timedelta(days=i)).strftime("%Y-%m-%d"), "count": 150 - (i * 10)}
        for i in range(7)
    ]