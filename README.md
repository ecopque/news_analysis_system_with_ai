# News Analysis System with AI

This project is designed to collect, analyze, and summarize news articles using AI. It integrates multiple news sources for collection and uses AI models such as **DeepSeek** and **Gemini** for analyzing the content.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure Diagram](#project-structure-diagram)
- [License](#license)

## Project Overview

The **News Analysis System with AI** is a tool to scrape and collect news from various sources, and then apply AI models to analyze, summarize, and generate insights based on the collected news articles.

Key features include:
- Collecting news from **RSS feeds** and **scraping websites**.
- **DeepSeek AI** integration for detailed analysis.
- **Gemini AI** for summarization, sentiment analysis, and trend identification.
- A **Streamlit-based dashboard** to display news and AI analysis results.

## Project Structure

Below is the directory structure for the project:

```plaintext
news_analyzer/
├── .env # Stores the API Key
├── .gitignore # Git ignore file
├── config/
│ └── sources.py # List of sites for scraping
├── dashboard/
│ ├── app_deepseek.py # Streamlit dashboard for DeepSeek AI
│ ├── app_gemini.py # Streamlit dashboard for Gemini AI
├── prints/ # Screenshots and images (not included in Git)
├── scripts/
│ ├── ai_client.py # Integration with AI services (DeepSeek and Gemini)
│ ├── collector.py # News collection (scraping/RSS)
├── venv_news/ # Virtual environment (not included in Git)
├── diagram_text.txt # Project structure diagram
├── log.txt # Log file for debugging
└── test_api.py # API testing script
