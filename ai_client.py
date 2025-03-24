# FILE: /ai_client.py

# [DeepSeek]:
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DeepSeekAI:
    def __init__(self):
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        self.base_url = 'https://api.deepseek.com/v1/chat/completions'