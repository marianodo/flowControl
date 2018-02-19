"""
Demo Flask application to test the operation of Flask with socket.io
Aim is to create a webpage that is constantly updated with random numbers from a background python process.
30th May 2014
"""

# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event


from sensor.flowSensor import FlowSensor
from storage.db import Database
import logging
from enum import IntEnum
logger = logging.getLogger(__name__)
from gevent import monkey
monkey.patch_all()
__author__ = 'slynn'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()
GPIO = [0, 4, 17, 27, 22, 18]
class RandomThread(Thread):
    def __init__(self):
		self.delay = 1
		self.db = Database()
		self.tapControl = [None]
		for tapId in range(1, 6):
			liters, label = self.db.getTapInfo(tapId)
			flowSensor = FlowSensor(tapId, GPIO[tapId], liters, label)
			self.tapControl.append(flowSensor)
		super(RandomThread, self).__init__()

    def getTapInfo(self, tapId):
		label = self.tapControl[tapId].getLabel()
		liters = self.tapControl[tapId].getLiters()
		return label, liters
    
    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print "Making random numbers"
        while not thread_stop_event.isSet():
			tapsInfo = {}
			for tapId in range(1, 6): #TODO Replace 5 for some constant or tapControl
				label, liters = self.getTapInfo(tapId)
				tapsInfo[tapId] = {}
				tapsInfo[tapId]["label"] = label
				tapsInfo[tapId]["liters"] = liters

			socketio.emit('newnumber', {'number': tapsInfo}, namespace='/test')
			socketio.sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print "Starting Thread"
        thread = RandomThread()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=1122)