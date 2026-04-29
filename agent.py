import os
import time
from google import genai
from google.api_core import exceptions
from scraper import get_trending_repos
from dotenv import load_dotenv

load_dotenv(override=True)

def run_agent():
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    raw_data = get_trending_repos()
    
    # Try the request up to 3 times if rate limited
    for attempt in range(3):
        try:
            # # Temporary debug: Print all available models
            # for m in client.models.list():
            #     print(f"Available Model: {m.name}")
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite", 
                contents=f"Summarize these trending repos: {raw_data}"
            )
            return response.text
            
        except Exception as e:
            if "429" in str(e):
                print(f"Rate limit hit. Retrying in 30 seconds... (Attempt {attempt + 1}/3)")
                time.sleep(30)
            else:
                return f"An unexpected error occurred: {e}"
    
    return "Failed to get a response after multiple retries due to quota limits."