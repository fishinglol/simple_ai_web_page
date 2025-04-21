from flask import Flask, render_template, jsonify, request
from google import genai
import os
from dotenv import load_dotenv

app = Flask(__name__)


load_dotenv()


API_KEY = os.getenv('GENAI_API_KEY')


if not API_KEY:
    raise ValueError("API_KEY is missing or not loaded properly")


client = genai.Client(api_key=API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_ai_response', methods=['POST'])
def get_ai_response():

    user_message = request.json.get('message', '')


    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=user_message
    )
    generated_content = response.text


    return jsonify({'ai_response': generated_content})

if __name__ == '__main__':
    app.run(debug=True)
