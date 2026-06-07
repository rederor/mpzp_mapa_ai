import os
import requests

class _GenerateContentConfig:
    def __init__(self, temperature=0.2, **kwargs):
        self.temperature = temperature
        self.kwargs = kwargs

class types:
    GenerateContentConfig = _GenerateContentConfig

class _Response:
    def __init__(self, text):
        self.text = text

class _Models:
    def __init__(self, api_key, base_url, default_model):
        self.api_key = os.getenv('DEEPSEEK_API_KEY') or api_key
        self.base_url = (os.getenv('DEEP