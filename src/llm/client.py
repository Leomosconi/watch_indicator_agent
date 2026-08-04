import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GPT_API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def get_response(self, prompt: str) -> str:
        try:
            response = self.client.responses.create(
                model='gpt-5.6-luna',
                input=prompt,
            )
            return response
        except Exception as e:
            print('Erro ao obter resposta do LLM:', e)


