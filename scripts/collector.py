# FILE: /scripts/collector.py

# [News Collector Implementation]:
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
from datetime import datetime
import time
from urllib.parse import urljoin

class NewsCollector:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrape_site(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = list()

            for i1 in soup.select('article')[:10]:
                title = i1.find('h2').text.strip() if i1.find('h2') else 'Untitled'
                link = i1.find('a')['href'] if i1.find('a') else '#'
                link = urljoin(url, link)

                articles.append({
                    'title': title,
                    'url': link,
                    'source': url,
                    'date': datetime.now().strftime('%Y-%m-%d')
                })
            
            return pd.DataFrame(articles)

        except Exception as my_error:
            print(f'Error: Error fetching {url}: {my_error}')

    def get_rss(self, feed_url):
        feed = feedparser.parse(feed_url)
        return pd.DataFrame([{
            'title': i2.title,
            'url': i2.link,
            'source': feed_url,
            'date': datetime.now().strftime('%Y-%m-%d')
        } for i2 in feed.entries[:15]])
    
    def run(self, sources):
        