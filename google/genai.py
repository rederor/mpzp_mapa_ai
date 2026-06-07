"""Minimalny adapter zgodnosci z google.genai dla DeepSeek API.

Pozwala pozostawic w aplikacji dotychczasowe wywolania:
    client.models.generate_content(...)
    genai.types.GenerateContentConfig(temperature=...)

Klucz API mozna podac jako argument Client(api_key=...) albo przez
zmienna srodowiskowa DEEPSEEK_API_KEY. Jezeli w aplikacji zostanie
placeholder "...", adapter sprobuje uzyc zmiennej srodowiskowej.