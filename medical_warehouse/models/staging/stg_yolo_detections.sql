-- medical_warehouse/models/staging/stg_yolo_detections.sql
WITH raw_detections AS (
    SELECT * FROM {{ source('public', 'raw_yolo_detections') }}
)

SELECT
    detection_id,
    message_id,
    UPPER(detected_item) AS detected_item, -- Standardize labels
    confidence_score,
    detected_at
FROM raw_detections
WHERE confidence_score > 0.5 -- Data Quality filter