# FILE: /dashboard/app_deepseek.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# [Dashboard with Streamlt]:
import streamlit as st #32:
import pandas as pd
from scripts.collector import NewsCollector #33:
from scripts.ai_client import DeepSeekAI

from config.sources import NEWS_SOURCES

# Page setup:
st.set_page_config(page_title='News Analyzer DeepSeek', layout='wide') #34:
st.title('News Analyzer with DeepSeek') #35:

# Sidebar for settings:
st.sidebar.header('Configurations') #36:
temperature = st.sidebar.slider( #37:
    'Temperature (creativity)',
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

# News gathering section:
st.header('News gathering') #38:
if st.button('Search for current news'): #39:
    collector = NewsCollector() #40:
    news_df = collector.run(NEWS_SOURCES)

    if not news_df.empty:
        st.session_state.news_df = news_df #41:
        st.success(f'Collected {len(news_df)} news!')
    else:
        st.error('No news was collected. Check sources.')

# Analysis section:
if 'news_df' in st.session_state: #42:
    st.header('Collected news') #43:
    st.dataframe(st.session_state.news_df) #44:

    st.header('AI Analysis') #45:
    if st.button('Analyze with DeepSeek'): #46:
        if not st.session_state.news_df.empty: #47:
            deepseek = DeepSeekAI()

            # Select 3 random news items for analysis:
            sample_news = st.session_state.news_df.sample(3) #48:

            # Prepare the text for analysis:
            analysis_text = ''
            for index, row in sample_news.iterrows(): #49:
                analysis_text += f'Title: {row["title"]}\nURL: {row["url"]}\n\n' #50:

            # Call the DeepSeek API:
            with st.spinner('Analyzing with DeepSeek...'): #51:
                analysis_result = deepseek.analyze(analysis_text, temperature) #52:
            
            st.subheader('Analysis Result')
            st.write(analysis_result)
        
        else:
            st.warning('No news available for analysis.')