
from flask import Flask, request, jsonify, render_template
import openai


app = Flask(__name__)

# Set your OpenAI GPT-3.5 API key
api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

# Define the route for code conversion
@app.route('/convert', methods=['POST'])
def convert_code():
    try:

        openai.api_key = api_key
        # Get the selected language from the request
        selected_language = request.json['language']
        code =request.json['code']

        
        # Use OpenAI GPT-3 to generate code conversion options
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or use the appropriate engine
            prompt=f"Convert the {code} to {selected_language}: ",
            max_tokens=500, # Adjust the number of tokens as needed
            # temperature=1
        )

        # Extract the generated code conversion options
        code_options = response.choices[0].text

        # You may want to perform some quality checks on code_options

        return jsonify({'code_options': code_options})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
