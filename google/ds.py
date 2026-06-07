import os
import requests

U = 'https://api.deepseek.com/chat/completions'
M = 'deepseek-chat'

def q(k, c, config=None):
    key = k if k and k != '...' else os.getenv('DEEPSEEK_API_KEY')
    if not key:
        raise RuntimeError('Brak klucza DeepSeek: ustaw DEEPSEEK_API_KEY albo wpisz API_KEY w aplikacji.')
    temp = getattr(config, 'temperature', 0.2) if config else 0.2
    r = requests.post(