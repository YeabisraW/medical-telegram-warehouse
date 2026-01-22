import os
import json
import logging
import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv
from datetime import datetime

# 1. Setup Logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/scraping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')

# List of target channels
CHANNELS = ['@CheMed123', '@lobelia4cosmetics', '@tikvahpharma']

async def scrape_channel(client, channel_username):
    logging.info(f"Starting scrape for {channel_username}")
    
    # Path for today's raw data
    date_str = datetime.now().strftime('%Y-%m-%d')
    json_dir = f"data/raw/telegram_messages/{date_str}"
    img_dir = f"data/raw/images/{channel_username.replace('@', '')}"
    
    os.makedirs(json_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)
    
    messages_data = []
    
    try:
        async for message in client.iter_messages(channel_username, limit=100):
            msg_info = {
                'message_id': message.id,
                'channel_name': channel_username,
                'message_date': str(message.date),
                'message_text': message.text,
                'has_media': message.media is not None,
                'views': message.views or 0,
                'forwards': message.forwards or 0,
            }
            
            # Download images if they exist
            if message.photo:
                img_path = await client.download_media(
                    message.photo, 
                    file=f"{img_dir}/{message.id}.jpg"
                )
                msg_info['image_path'] = img_path
            
            messages_data.append(msg_info)

        # Save to JSON
        filename = f"{json_dir}/{channel_username.replace('@', '')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(messages_data, f, indent=4, ensure_ascii=False)
            
        logging.info(f"Successfully saved {len(messages_data)} messages for {channel_username}")

    except Exception as e:
        logging.error(f"Error scraping {channel_username}: {str(e)}")

async def main():
    async with TelegramClient('scraping_session', api_id, api_hash) as client:
        tasks = [scrape_channel(client, channel) for channel in CHANNELS]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())