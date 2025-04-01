# FILE: /scripts/ai_client.py

# [DeepSeek]:
import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# [DEEP SEEK]
class DeepSeekAI:
    def __init__(self):
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        self.base_url = 'https://api.deepseek.com/v1/chat/completions'

    def analyze(self, text, temperature=0.7):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            'model': 'deepseek-chat',
            'messages': [{
                    'role': 'user',
                    'content': f'Analyze this text: {text}'
                }],
            'temperature': temperature,
            'max_tokens': 1000
        }
        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()

            response_data = response.json()
            print(f'API response: {response_data}')
            if 'choices' not in response_data:
                return f"API error: Unexpected response - {response_data.get('message', 'No details')}"
            
            return response_data['choices'][0]['message']['content']
        
        except Exception as my_error:
            
            return f'Error: {my_error}.'
        

# [GOOGLE AI]
class GeminiChat:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.chat = None
        self.context = '''
        You are an assistant specializing in news analysis.

        Help users understand the data they collect with:
        - Concise summaries
        - Sentiment analysis
        - Trend identification
        '''

    def start_chat(self, news_data):
        self.chat = self.model.start_chat()
        self.chat.send_message(
            f'{self.context}\n\nCurrent data: (format JSON):\n{news_data}'
        )

    def ask (self, question):
        if not self.chat:
            return 'Error: Chat not started.'
        
        response = self.chat.send_message(question)
        return response.text