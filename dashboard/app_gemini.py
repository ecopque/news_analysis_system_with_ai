# FILE: /dashboard/app_gemini.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from scripts.collector import NewsCollector
from scripts.ai_client import GeminiChat
from config.sources import NEWS_SOURCES

# Streamlit config:
st.title('News Analyzer Gemini')

# Sidebar:
if 'chat' not in st.session_state:
    st.session_state.chat = GeminiChat()

# News collection:
if st.button('News Update'):
    with st.spinner('Collecting news...'):
        collector = NewsCollector()
        st.session_state.news_df = collector.run(NEWS_SOURCES)
        
        # Prepare text for chat
        news_text = ""
        for index, row in st.session_state.news_df.iterrows():
            news_text += f"Title: {row['title']}\nURL: {row['url']}\nSource: {row['source']}\nDate: {row['date']}\n\n"
        st.session_state.chat.start_chat(news_text)
    st.success('News ready for analysis.')

# Chat:
if 'news_df' in st.session_state:
    st.subheader('Ask about the news')
    user_question = st.text_input('Ask a question about the news:')
    if user_question:
        with st.spinner('Generating response...'):
            response = st.session_state.chat.ask(user_question)
        st.write(response)

# Analysis section:
if 'news_df' in st.session_state:
    st.header('Collected news')
    st.dataframe(st.session_state.news_df)

    st.header('Gemini Analysis')
    if st.button('Analyze with Gemini'):
        if not st.session_state.news_df.empty:
            # Prepare text for analysis:
            analysis_text = ""
            for index, row in st.session_state.news_df.iterrows():
                analysis_text += f"Title: {row['title']}\nURL: {row['url']}\nSource: {row['source']}\nDate: {row['date']}\n\n"

            with st.spinner('Analyzing with Gemini...'):
                analysis_result = st.session_state.chat.ask(f'Summarize and analyze the sentiment of the following news: {analysis_text}')

            st.subheader('Gemini Analysis Result')
            st.write(analysis_result)

        else:
            st.warning('No news available for analysis.')