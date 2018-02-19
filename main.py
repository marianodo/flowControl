from sensor.flowSensor import FlowSensor
from storage.db import Database
import logging
from enum import IntEnum
logger = logging.getLogger(__name__)

#TAP N 1   2   3   4   5
GPIO = [0, 4, 17, 27, 22, 18] #Configure GPIO from sensors. The position of the array is the tap id, and the value is the GPIO

class Main(Thread):
	def __init__(self):
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

	def getAllTaps(self):
		tapsInfo = {}
		for tapId in range(1, 6): #TODO Replace 5 for some constant or tapControl
			label, liters = self.getTapInfo(tapId)
			tapsInfo[tapId] = {}
			tapsInfo[tapId]["label"] = label
			tapsInfo[tapId]["liters"] = liters

		return tapsInfo