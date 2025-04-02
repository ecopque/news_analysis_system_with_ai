# News Analysis System with AI

This project is designed to collect, analyze, and summarize news articles using AI. It integrates multiple news sources for collection and uses AI models such as **DeepSeek** and **Gemini** for analyzing the content. The system **interacts with the AI** to provide insights about the news content and also allows users to download the news data in **JSON** format.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Images](#images)
- [Project Structure Diagram](#project-structure-diagram)
- [Developer Guide](#developer-guide)
- [About the Author](#developer-info)

## Project Overview

The **News Analysis System with AI** is a tool to scrape and collect news from various sources, and then apply AI models to analyze, summarize, and generate insights based on the collected news articles.

Key features include:
- Collecting news from **RSS feeds** and **scraping websites**.
- **DeepSeek AI** integration for detailed analysis.
- **Gemini AI** for summarization, sentiment analysis, and trend identification.
- **Interaction with AI models** to understand and analyze news content.
- Ability to **download the collected news in JSON format** for further processing or use.

## Technologies Used

- **Python**: Primary programming language.  
- **Streamlit**: Web framework for building the interactive dashboard.  
- **Requests**: HTTP requests to fetch data from APIs.  
- **BeautifulSoup4**: Web scraping for parsing HTML content.  
- **Feedparser**: Parsing RSS feeds for news aggregation.  
- **Pandas**: Data manipulation and structuring.  
- **Python-dotenv**: Managing environment variables securely.  

## Installation

To set up the project, follow these steps:

### 1. Clone the repository
Clone the project to your local machine:

```bash
git clone https://github.com/yourusername/news_analysis_system_with_ai.git
cd news_analysis_system_with_ai
```

### 2. Set up a virtual environment
Create and activate a virtual environment:

```bash
python3 -m venv venv_news
source venv_news/bin/activate  # Linux/macOS
venv_news\Scripts\activate  # Windows
```

### 3. Install dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```
If you don’t have a requirements.txt file, manually install the dependencies:
```bash
pip install requests beautifulsoup4 feedparser pandas python-dotenv streamlit
```

### 4. Set up environment variables
Create a .env file in the root directory and add your API keys:
```bash
DEEPSEEK_API_KEY=your_deepseek_api_key
GEMINI_API_KEY=your_gemini_api_key
```

## Usage

### 1. Running the Streamlit App
Run the Gemini-based Streamlit app:
```bash
streamlit run dashboard/app_gemini.py
```
Or the DeepSeek-based Streamlit app:
```bash
streamlit run dashboard/app_deepseek.py
```

### 2. Collecting and Analyzing News
- News Update: Click the "News Update" button to collect the latest news.
- Analysis: Use the Gemini or DeepSeek AI model to analyze and summarize the news content.

### 3. Downloading the Collected News
Once the news is collected, you can download the data in JSON format for further processing.

## Images
This section provides visual examples of the program in action. You can find screenshots of the dashboard, news collection, and analysis sections.
![x]()
![x]()
![x]()
![x]()
![x]()
![x]()

## Project Structure Diagram
For easy reference, here is the current project structure:
```bash
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
```

## Developer Guide

If you have any questions about the code, I have documented the most important lines with explanations on their functionality in the **log.txt** file. This file provides a **step-by-step** guide to help understand the code and how the system works.

## About the Author

    . Developer: Edson Copque
    . Website: https://linktr.ee/edsoncopque
    . GitHub: https://github.com/ecopque
    . Signal Messenger: ecop.01