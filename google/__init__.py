from pkgutil import extend_path

# Pozwala lokalnemu modułowi google.genai działać jako warstwa zgodności,
# nie odcinając jednocześnie ewentualnych innych pakietów z przestrzeni google.*.
__path__ = extend_path(__path__, __name__)
