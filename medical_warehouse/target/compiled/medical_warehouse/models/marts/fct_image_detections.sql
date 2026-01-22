

WITH messages AS (
    SELECT 
        message_id, 
        channel_id, 
        message_text, 
        image_path,
        created_at
    FROM "medical_db"."analytics"."stg_telegram_messages" -- Replace with your actual staging model
),
detections AS (
    SELECT 
        image_path,
        detected_item,
        confidence
    FROM "medical_db"."analytics"."stg_yolo_detections" -- Replace with your actual staging model
)

SELECT
    m.message_id,
    m.channel_id,
    m.message_text,
    d.detected_item,
    d.confidence,
    -- Requirement: image_category logic
    CASE 
        WHEN d.detected_item IN ('pill', 'tablet', 'syrup') THEN 'Medicine'
        WHEN d.detected_item IN ('syringe', 'mask', 'gloves') THEN 'Equipment'
        ELSE 'Other'
    END AS image_category,
    m.created_at
FROM messages m
LEFT JOIN detections d ON m.image_path = d.image_path