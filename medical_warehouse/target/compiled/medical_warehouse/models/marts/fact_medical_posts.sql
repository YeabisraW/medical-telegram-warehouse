

with staging as (
    select * from "medical_db"."analytics"."stg_telegram_messages"
)

select
    message_id,
    channel_name,
    message_at,
    message_text,
    views,
    forwards,
    -- Simple formula to weight engagement
    (views + (forwards * 10)) as engagement_score
from staging