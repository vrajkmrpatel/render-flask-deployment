from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai

# Load API_KEY from .env file
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow requests from React frontend

# Configure Google Generative AI API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Endpoint for text generation


@app.route("/api/generate", methods=["POST"])
def generate_text():
    data = request.json
    print("Received data:", data)  # Debugging
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Use Google Generative AI model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        generated_text = response.text.strip()
        return jsonify({"text": generated_text})
    except Exception as e:
        print("Error:", str(e))  # Debugging
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
