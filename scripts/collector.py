# FILE: /scripts/collector.py

# [News Collector Implementation]:
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
from datetime import datetime
import time
from urllib.parse import urljoin

