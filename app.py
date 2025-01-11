from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        # Generate a response from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"User: {user_message}\nBot:",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        bot_message = response["choices"][0]["text"].strip()
        return jsonify({"message": bot_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
