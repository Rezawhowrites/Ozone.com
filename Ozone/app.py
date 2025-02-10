from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
import ollama

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.form.get('chat')
        responce = ollama.generate(model='llama3.2:1b', prompt=f"{user_message}. Reply in less tokens.") ["response"] 
        user_message = user_message.capitalize()
        with open("chat_history.txt","a") as file:
            file.write(f"[[[[User: {user_message}\nBOT: {responce}]]]]\n\n")
            
        if user_message:
            # Append user message
            messages.append({'sender': 'user', 'text': user_message})
            # Generate bot response (placeholder)
            bot_response = responce
            messages.append({'sender': 'bot', 'text': bot_response})
        return redirect(url_for('index'))

    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
