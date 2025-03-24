# FILE: /test_api.py

# [Teste the API in isolation]:
from scripts.ai_client import DeepSeekAI
from dotenv import load_dotenv

load_dotenv()

deepseek = DeepSeekAI()
test_text = 'API connection text.'
result = deepseek.analyze(test_text)
print('Result:', result)