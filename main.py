from sensor.flowSensor import FlowSensor
from storage.db import Database
import logging
from enum import IntEnum
from threading import Thread, Event
import time
logger = logging.getLogger(__name__)

thread_stop_event = Event()
threads = list()
START_TAP = 1
MAX_TAP_AMOUNT = 5
#TAP N 1   2   3   4   5
GPIO = [0, 4, 17, 27, 22, 18] #Configure GPIO from sensors. The position of the array is the tap id, and the value is the GPIO
class Main(Thread):
	def __init__(self, socketio):
		self.socketio = socketio
		
		
		self.listenSockets(socketio)

		self.delay = 1
		self.db = Database()
		self.tapControl = [None]
		self.timeToStorage = 0
		for tapId in range(START_TAP, MAX_TAP_AMOUNT + 1):
			liters, label = self.db.getTapInfo(tapId)
			flowSensor = FlowSensor(tapId, GPIO[tapId], liters, label)
			self.tapControl.append(flowSensor)

		super(Main, self).__init__()

	def getTapInfo(self, tapId):
		label = self.tapControl[tapId].getLabel()
		liters = self.tapControl[tapId].getLiters()
		return label, liters
    
	def startMeasuring(self):
		while not thread_stop_event.isSet():
			tapsInfo = {}
			for tapId in range(START_TAP, MAX_TAP_AMOUNT + 1): 
				label, liters = self.getTapInfo(tapId)
				tapsInfo[tapId] = {}
				tapsInfo[tapId]["label"] = label
				tapsInfo[tapId]["liters"] = liters

				if self.timeToStorage == 10:
					self.db.updateTapLiters(tapId, liters)
					
			if self.timeToStorage == 10:
				self.timeToStorage = 0
			self.socketio.emit('tapFlow', {'taps': tapsInfo}, namespace='/test')
			self.socketio.sleep(self.delay)
			self.timeToStorage += 1

	def storageData(self):
		while True:
			for tapId in range(START_TAP, MAX_TAP_AMOUNT + 1): 
				_, liters = self.getTapInfo(tapId)
				
			time.sleep(10)

	
	def listenSockets(self, socketio):
		@socketio.on('resetTap', namespace='/test')
		def test_disconnect(msg):
			self.db.resetTap(msg["data"])
			self.tapControl[msg["data"]].clearPulse()


	def run(self):
		self.startMeasuring()
