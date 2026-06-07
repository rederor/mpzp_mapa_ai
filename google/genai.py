import os, requests

class _Cfg:
    def __init__(self, temperature=0.2, **kw):
        self.temperature = temperature

class types:
    GenerateContentConfig = _Cfg

class _Resp:
    def __init__(self, text):
        self.text = text

class _Models:
    def __init__(self, key):
        self.key = os.getenv('DEEPSEEK_API_KEY') or key
        base = os.getenv('DEEPSEEK_BASE_URL') or 'https://api.deepseek