from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import vertexModTxtBison

app = Flask(__name__,template_folder='Templates')
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(message):
    print('Your question:', message)

    # Process the message (e.g., send it to a chatbot)
    # In this example, we'll just send the message back to the client
    emit('receive_message', message)
    #answer = vertexModTxtBison.vertexAiQes(message)
    #emit('receive_answer', answer)

def main():
    if __name__ == '__main__':
    socketio.run(app, host= "0.0.0.0", port=8080)
