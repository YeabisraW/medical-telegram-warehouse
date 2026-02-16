import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Medical Analytics", page_icon="💊")
st.title("Medical Telegram Insights")

# Fetch data from YOUR FastAPI
try:
    response = requests.get("http://localhost:8000/analytics/summary")
    summary = response.json()
    
    col1, col2 = st.columns(2)
    col1.metric("Total Processed", summary['total_messages_processed'])
    col2.metric("Sentiment Score", summary['average_sentiment'])
    
    # Trends Chart
    trends_res = requests.get("http://localhost:8000/analytics/trends")
    df = pd.DataFrame(trends_res.json())
    st.line_chart(df.set_index('date'))

except:
    st.warning("API not detected. Start FastAPI to see real-time data.")