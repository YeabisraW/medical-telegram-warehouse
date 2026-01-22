from fastapi import Query

# 1. Pydantic Schema for Search
class MessageSearchResponse(BaseModel):
    message_id: int
    channel_id: str
    message_text: str
    detected_item: Optional[str]

# 2. Search Endpoint with Pagination (Requirement #1)
@app.get("/analytics/search", response_model=List[MessageSearchResponse])
def search_messages(
    query: str = Query(..., min_length=3, description="Text to search for"),
    limit: int = 10,
    offset: int = 0
):
    conn = get_db_connection()
    with conn.cursor() as cur:
        # Using ILIKE for case-insensitive search
        cur.execute("""
            SELECT message_id, channel_id, message_text, detected_item 
            FROM fct_image_detections 
            WHERE message_text ILIKE %s
            LIMIT %s OFFSET %s
        """, (f'%{query}%', limit, offset))
        return cur.fetchall()

# 3. Visual Content Report (Requirement #1)
@app.get("/analytics/visual-report")
def get_visual_report():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT image_category, COUNT(*) as count, AVG(confidence) as avg_confidence
            FROM fct_image_detections
            GROUP BY image_category
        """)
        return cur.fetchall()