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
            response = requests.get(url, headers=self.headers, timeout=10) #5:
            soup = BeautifulSoup(response.text, 'html.parser') #6:
            articles = list()

            for i1 in soup.find_all('articles'): #7:
                if len(articles) >= 10:
                    break

                title = 'Untitled'
                if i1.find('h2'): #8:
                    title = i1.find('h2').text.strip() #9:

                link = '#'
                if i1.find('a'): #10:
                    link = i1.find('a')['href'] #11:
                    link = urljoin(url, link) #12:
            
                articles.append({
                    'title': title,
                    'url': link,
                    'source': url,
                    'date': datetime.now().strftime('%Y-%m-%d')
                })
            return pd.DataFrame(articles) #13:

        except Exception as my_error:
            print(f'Error: Error fetching {url}: {my_error}')
            return pd.DataFrame() #14:

    def get_rss(self, feed_url):
        feed = feedparser.parse(feed_url) #15:
        articles = list()

        for i2 in feed.entries: #16:
            if len(articles) >= 15:
                break
        
            articles.append({
                'title': i2.title,
                'url': i2.link,
                'source': feed_url,
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return pd.DataFrame(articles) #17:

    def run(self, sources):
        all_news = pd.DataFrame() #18:

        for i3 in sources:
            if i3.endswith('.xml'): #19:
                df = self.get_rss(i3) #20:
            else:
                df = self.scrape_site(i3) #21:
            
            all_news = pd.concat([all_news, df]) #22:
            time.sleep(2)
        return all_news.drop_duplicates('url') #23: