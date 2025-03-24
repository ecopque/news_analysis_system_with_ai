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

    def analyze(self, text, temperature=0.7):
        hreaders = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            'model': 'deepseek-chat',
            'messages': [
                {
                    'role': 'user',
                    'content': f'Analyze this text: {text}'
                }
            ],
            'temperature': temperature,
            'max_tokens': 1000
        }