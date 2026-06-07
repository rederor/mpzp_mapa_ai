import os
import requests

class types:
    class GenerateContentConfig:
        def __init__(self, temperature=0.2, **kwargs):
            self.temperature = temperature

class _Response:
    def __init__(self, text):
        self.text = text

class Client:
    def __init__(self, api_key=None):
        self.api_key = api_key if api_key and api_key != "..." else os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("Brak klucza API