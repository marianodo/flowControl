from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from main import Main
main = Main()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=1122)

    socketio.run(app, host='0.0.0.0', port=1122)
