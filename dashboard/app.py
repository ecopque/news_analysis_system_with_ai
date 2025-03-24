# FILE: /dashboard/app.py

# [Dashboard with Streamlt]:
import streamlit as st #32:
import pandas as pd
from scripts.collector import NewsCollector #33:
from config.sources import NEW_SOURCES

# Page setup:
st.set_page_config(page_title='News Analyzer', layout='wide')
st.title('News Analyzer with DeepSeek')

# Sidebar for settings:
st.sidebar.header('Confugurations')
temperature = st.sidebar.slider(
    'Temperature (creativity)',
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)