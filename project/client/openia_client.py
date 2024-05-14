from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def analyze_tweets(self, review):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"""Basado en el siguiente resumen de tweets:\n\n{review}\nRealiza un 
                análisis que incluya: 1. Evaluación del sentimiento general hacia el tema/partido/entidad mencionada. 2. 
                Análisis de la ideología presente en las discusiones. 3. Estimación de la media de engagement de estas 
                publicaciones. 4. Probabilidad de sesgos de confirmación en las discusiones. 5. Probabilidad de sesgos 
                de bandwagon en la opinión pública."""}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
