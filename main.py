from sensor.flowSensor import FlowSensor
from storage.db import Database
import logging
from enum import IntEnum
logger = logging.getLogger(__name__)

FIRST_TAP  = (1, 4) #First value is tap position. Second value is GPIO of sensors
SECOND_TAP = (2, 0) #CHANGE THIS VALUES
THIRD_TAP  = (3, 0)
FOURTH_TAP = (4, 0)
FIFTH_TAP  = (5, 0)
POS = 0
GPIO = 1

getLitersFromDB = [0,0,0,0,0]
class Main(object):
	def __init__(self):
		self.db = Database()
		self.initFlowSensors()

		tapControl =   [None, FlowSensor(FIRST_TAP[POS], FIRST_TAP[GPIO], getLitersFromDB[FIRST_TAP[POS]]),
						FlowSensor(SECOND_TAP[POS], SECOND_TAP[GPIO], getLitersFromDB[SECOND_TAP[POS]]),
						FlowSensor(THIRD_TAP[POS], THIRD_TAP[GPIO], getLitersFromDB[THIRD_TAP[POS]]),
						FlowSensor(FOURTH_TAP[POS], FOURTH_TAP[GPIO], getLitersFromDB[FOURTH_TAP[POS]]),
						FlowSensor(FIFTH_TAP[POS], FIFTH_TAP[GPIO], getLitersFromDB[FIFTH_TAP[POS]])]
