from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# 1. DEFINE THE APP FIRST
app = FastAPI(title="Medical Telegram Warehouse API")

# 2. DEFINE YOUR MODELS
class MessageSearchResponse(BaseModel):
    id: int
    channel_title: str
    message_text: str
    detected_item: Optional[str]
    confidence: Optional[float]

# 3. DEFINE YOUR ROUTES
@app.get("/analytics/search", response_model=List[MessageSearchResponse])
async def search_messages():
    # Your database logic here
    return []