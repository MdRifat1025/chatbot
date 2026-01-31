import os
import groq
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
groq.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt):
    """
    Sends the user prompt to OpenAI GPT model and returns the response.
    """
    try:
        response = groq.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("OpenAI API error:", e)
        return "Sorry, something went wrong with the AI."
