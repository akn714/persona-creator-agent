import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class GroqLLM:
    model = "llama-3.3-70b-versatile"

    def __init__(self):
        """
        Initialize the GroqLLM
        """
        print('[+] Initializing GroqLLM...')
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def get_llm_response(self, messages):
        """
        Get the response from the LLM
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        output = response.choices[0].message.content.strip()

        if output and (output[0] == output[-1]) and output.startswith(("'", '"')):
            output = output[1:-1]

        return output

llm = GroqLLM()

