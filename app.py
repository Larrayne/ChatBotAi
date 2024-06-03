import os
from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    try: 
        # Call OpenAI API with the message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[

                {"role": "user", "content": message}
            ]
        )

        answer= response.choices[0].message

        return jsonify({'response': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
