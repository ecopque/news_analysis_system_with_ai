# FILE: /dashboard/app.py

# [Dashboard with Streamlt]:
import streamlit as st #32:
import pandas as pd
from scripts.collector import NewsCollector #33:
from config.sources import NEW_SOURCES

# Page setup:
st.set_page_config(page_title='News Analyzer', layout='wide') #34:
st.title('News Analyzer with DeepSeek') #35:

# Sidebar for settings:
st.sidebar.header('Confugurations') #36:
temperature = st.sidebar.slider( #37:
    'Temperature (creativity)',
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

# News gathering section:
st.header('News Collect') #38:
if st.button('Search for current news'): #39:
    collector = NewsCollector() #40:
    news_df = collector.run(NEW_SOURCES)

    if not news_df.empty:
        st.session_state.news_df = news_df #41:
        st.success(f'Collected {len(news_df)} news!')
    else:
        st.error('No news was collected. Check sources.')

# Analysis section:
if 'news_df' in st.session_state: #42:
    st.header('Collected news') #43:
    st.dataframe(st.session_state.news_df) #44: