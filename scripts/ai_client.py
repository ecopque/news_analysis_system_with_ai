# FILE: /scripts/ai_client.py

# [DeepSeek]:
import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

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
        self.chat = self.model.start_chat() #54:
        self.chat.send_message(
            f'{self.contexto}\n\nCurrent data: (format JSON):\n{news_data}'
        ) #55:

    def ask (self, question):
        if not self.chat:
            return 'Error: Chat not started.'
        
        response = self.chat.send_message(question)
        return response.text


# [DEEP SEEK]
class DeepSeekAI:
    def __init__(self):
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        self.base_url = 'https://api.deepseek.com/v1/chat/completions' #24:

    def analyze(self, text, temperature=0.7): #25:
        headers = {
            "Authorization": f"Bearer {self.api_key}", #26:
            "Content-Type": "application/json" #27:
        }

        payload = {
            'model': 'deepseek-chat',
            'messages': [{
                    'role': 'user',
                    'content': f'Analyze this text: {text}' #28:
                }],
            'temperature': temperature,
            'max_tokens': 1000 #29:
        }
        try:
            response = requests.post(self.base_url, headers=headers, json=payload) #30:
            response.raise_for_status() #53:

            response_data = response.json() #30:
            print(f'API response: {response_data}') #54:
            if 'choices' not in response_data: #55:
                return f"API error: Unexpected response - {response_data.get('message', 'No details')}" #56:
            
            return response_data['choices'][0]['message']['content'] #31:
        
        except Exception as my_error:
            return f'Error: {my_error}.'