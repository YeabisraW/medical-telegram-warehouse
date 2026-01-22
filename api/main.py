from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from config import Config, logger
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="Medical Warehouse Analytics API")

# --- Pydantic Schemas (Requirement for Comment #1 & #4) ---
class DetectionSummary(BaseModel):
    detected_item: str
    count: int
    image_category: str

class ChannelActivity(BaseModel):
    channel_id: str
    message_count: int
    last_update: datetime

# --- Database Helper ---
def get_db_connection():
    try:
        return psycopg2.connect(Config.get_db_connection_string(), cursor_factory=RealDictCursor)
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")

# --- Analytical Endpoints ---

@app.get("/analytics/top-products", response_model=List[DetectionSummary])
def get_top_products():
    """Returns top detected medical products from the Mart model."""
    conn = get_db_connection()
    with conn.cursor() as cur:
        # We query the MART table we created in Step 3
        cur.execute("""
            SELECT detected_item, COUNT(*) as count, image_category
            FROM fct_image_detections
            WHERE detected_item IS NOT NULL
            GROUP BY detected_item, image_category
            ORDER BY count DESC
            LIMIT 10
        """)
        return cur.fetchall()

@app.get("/analytics/channel-activity", response_model=List[ChannelActivity])
def get_channel_activity():
    """Returns message volume per channel."""
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT channel_id, COUNT(*) as message_count, MAX(created_at) as last_update
            FROM fct_image_detections
            GROUP BY channel_id
        """)
        return cur.fetchall()