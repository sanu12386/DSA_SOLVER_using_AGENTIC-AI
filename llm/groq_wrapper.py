import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GroqLLM:
    def __init__(self, api_key: str = None, model: str = "llama3-8b-8192"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.model = model
        self.url = "https://api.groq.com/openai/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def generate(self, prompt: str) -> str:
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful DSA assistant."},
                {"role": "user", "content": prompt.strip()}
            ],
            "temperature": 0.4
        }

        response = requests.post(self.url, headers=self.headers, json=body)

        if not response.ok:
            print("❌ Error response content:", response.text)  # <== DEBUG info
            response.raise_for_status()

        return response.json()['choices'][0]['message']['content']
