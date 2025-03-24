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
