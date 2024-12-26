import os
import google.generativeai as genai

# Load API_KEY from .env file
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What is the capital of France??")
print(response.text)
