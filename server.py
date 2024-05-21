from flask import Flask, request, jsonify
import openai
import subprocess

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'SvQh3AYsCx4r2NqT3B1bkFJrjkD37tAaLquw95SWowm'

@app.route('/execute', methods=['POST'])
def execute_command():
    data = request.get_json()
    prompt = data.get('prompt')

    # Send the prompt to OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    # Extract the command from the response
    command = response.choices[0].text.strip()

    try:
        # Execute the command on the Ubuntu terminal
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

