import os
import psycopg2
from ultralytics import YOLO

# 1. Load YOLO model
model = YOLO('yolov8n.pt') 

# 2. DB Connection details
DB_CONFIG = {
    "dbname": "medical_db",
    "user": "postgres",
    "password": "password123",
    "host": "localhost",
    "port": "5432"
}

IMAGE_ROOT = "data/raw/images"
CHANNELS = ['CheMed123', 'lobelia4cosmetics', 'tikvahpharma']

def save_detections():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    for channel in CHANNELS:
        folder_path = os.path.join(IMAGE_ROOT, channel)
        if not os.path.exists(folder_path): continue
            
        print(f"--- Saving detections for: {channel} ---")
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png'))]
        
        for img_name in images:
            img_path = os.path.join(folder_path, img_name)
            results = model.predict(source=img_path, conf=0.25, verbose=False)
            
            for result in results:
                for box in result.boxes:
                    label = model.names[int(box.cls)]
                    conf = float(box.conf[0])
                    coords = box.xyxy[0].tolist() # [x_min, y_min, x_max, y_max]
                    
                    # Insert into Postgres
                    cur.execute("""
                        INSERT INTO raw.detections 
                        (image_path, channel_name, label, confidence, x_min, y_min, x_max, y_max)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (img_path, channel, label, conf, coords[0], coords[1], coords[2], coords[3]))
        
        conn.commit() # Commit after each channel
    
    cur.close()
    conn.close()
    print("✅ All detections saved to database!")

if __name__ == "__main__":
    save_detections()