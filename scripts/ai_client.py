# FILE: /scripts/ai_client.py

# [DeepSeek]:
import os
import requests #30:
from dotenv import load_dotenv #31:
import google.generativeai as genai

# Loading Environment Variables
load_dotenv() #32:

# [DEEP SEEK]
class DeepSeekAI:
    def __init__(self):
        self.api_key = os.getenv('DEEPSEEK_API_KEY') #33:
        self.base_url = 'https://api.deepseek.com/v1/chat/completions' #34:

    def analyze(self, text, temperature=0.7):
        
        # Creating Headers
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        } #35:

        # Creating the Payload (Request Data)
        payload = {
            'model': 'deepseek-chat',
            'messages': [{
                    'role': 'user',
                    'content': f'Analyze this text: {text}'
                }],
            'temperature': temperature,
            'max_tokens': 1000
        } #36:

        try:
            # Sending the Request to the API
            response = requests.post(self.base_url, headers=headers, json=payload) #37:
            response.raise_for_status() #38:

            # Processing the Response
            response_data = response.json() #39:
            print(f'API response: {response_data}')

            if 'choices' not in response_data: #40:
                return f"API error: Unexpected response - {response_data.get('message', 'No details')}"
            else:
                return response_data['choices'][0]['message']['content'] #41:
        
        except Exception as my_error:
            return f'Error: {my_error}.'
        

# [GOOGLE AI]
class GeminiChat:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY')) #42:
        self.model = genai.GenerativeModel('gemini-1.5-flash') #43:
        self.chat = None #44:
        self.context = '''
        You are an assistant specializing in news analysis.

        Help users understand the data they collect with:
        - Concise summaries
        - Sentiment analysis
        - Trend identification
        ''' #45:

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