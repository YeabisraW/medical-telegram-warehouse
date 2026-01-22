with raw_messages as (
    select * from {{ source('raw_data', 'telegram_messages') }}
)

select
    message_id::int as message_id,
    channel_name,
    -- Convert the date string to a real timestamp
    message_date::timestamp as message_at,
    message_text,
    -- Handle missing values
    coalesce(views, 0) as views,
    coalesce(forwards, 0) as forwards
from raw_messages
where message_id is not null