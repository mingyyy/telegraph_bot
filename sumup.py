import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def summarize_text(text):
    prompt = f"Summarize the following article in one paragraph:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
