import openai
from flask import Flask, request, jsonify, render_template
import traceback
import os

# Load your OpenAI API key (replace with your actual API key or use an env variable)
openai.api_key = "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"  # Replace with your actual API key

# Constants
MODEL_ENGINE = "gpt-3.5-turbo"
MESSAGE_SYSTEM = "You are a helpful assistant for my website"
messages = [{"role": "system", "content": MESSAGE_SYSTEM}]

# Initialize Flask app
app = Flask(__name__)

# Function to generate chat completion
def generate_chat_completion(user_input=""):
    # Append user input to the conversation
    messages.append({"role": "user", "content": user_input})
    try:
        # Make API call to OpenAI chat completions endpoint
        response = openai.chat.completions.create(
            model=MODEL_ENGINE,
            messages=messages,
            temperature=0.5,
            max_tokens=104
        )

        # Get the bot's response from the API (access 'content' from the message)
        bot_reply = response.choices[0].message
        bot_reply_content = bot_reply.content

        # Append the bot's response to the conversation
        messages.append(bot_reply)

        # Return the bot's response
        return bot_reply_content

        

    except Exception as e:
        print(f"Error generating chat completion: {str(e)}")
        return "Sorry, something went wrong. Please try again later."


@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle chat requests from the client (POST method)
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the request
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"reply": "Sorry, I didn’t understand that."})

        # Handle exit/quit commands
        if user_message.lower() in ['exit', 'quit']:
            return jsonify({"reply": "Goodbye! Feel free to reach out anytime.", "show_modal": True})

        # Generate the bot's response if not exit
        bot_reply = generate_chat_completion(user_message)
        bot_reply = str(bot_reply)

        # Return the bot's reply as a JSON response
        return jsonify({"reply": bot_reply, "show_modal": False})

    except Exception as e:
        print(f"Error: {str(e)}")
        print(traceback.format_exc())  # Log the traceback for better debugging
        return jsonify({"reply": "Sorry, something went wrong. Please try again later."}), 500
if __name__ == '__main__':
    app.run(debug=True)
