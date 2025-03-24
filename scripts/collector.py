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
        self.headers = {'User-Agent': 'Mozilla/5.0'} #4:

    def scrape_site(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            articles = list()

            for i1 in soup.find_all('articles'):
                if len(articles) >= 10:
                    break

                title = 'Untitled'
                if i1.find('h2'):
                    title = i1.find('h2').text.strip()

                link = '#'
                if i1.find('a'):
                    link = i1.find('a')['href']
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
            return pd.DataFrame()

    def get_rss(self, feed_url):
        feed = feedparser.parse(feed_url)
        articles = list()

        for i2 in feed.entries:
            if len(articles) >= 15:
                break
        
            articles.append({
                'title': i2.title,
                'url': i2.link,
                'source': feed_url,
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return pd.DataFrame(articles)

    def run(self, sources):
        all_news = pd.DataFrame()

        for i3 in sources:
            if i3.endswith('.xml'):
                df = self.get_rss(i3)
            else:
                df = self.scrape_site(i3)
            
            all_news = pd.concat([all_news, df])
            time.sleep(2)
        return all_news.drop_duplicates('url')