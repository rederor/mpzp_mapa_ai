from .ds import q

class types:
    class GenerateContentConfig:
        def __init__(self, temperature=0.2, **kwargs):
            self.temperature = temperature

class Client:
    def __init__(self, api_key=None):
        self.models = self
        self.api_key = api_key

    def generate_content(self, model, contents, config=None):
        return type('R', (), {'text': q(self.api_key, contents, config)})()
