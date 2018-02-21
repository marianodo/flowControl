from flask_socketio import SocketIO 
from flask import Flask, render_template

from main import Main
from sensor.flowSensor import FlowSensor
from storage.db import Database
import logging
from threading import Thread

logger = logging.getLogger(__name__)

from gevent import monkey
monkey.patch_all()

__author__ = 'Mariano Dominguez'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app)
thread = Thread()

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    if not thread.isAlive():
        thread = Main(socketio)
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)