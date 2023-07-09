from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return response

def generate_response(user_input):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
