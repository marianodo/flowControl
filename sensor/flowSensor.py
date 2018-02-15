import RPi.GPIO as GPIO
import time
import threading
import datetime as DT
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

class FlowSensor(object):
    def __init__(self,tapPosition, gpio, liters = 0):
        self.liters = liters
        self.pulse = 0
        self.tapPosition = tapPosition
        self.gpio = gpio
        self.configureGpioSensors()

    def configureGpioSensors(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.gpio, GPIO.RISING, callback=self.incrementPulse)

    def incrementPulse(self):
        self.pulse += 1
        self.getLiterAmountFromPulse()

    def getLiterAmountFromPulse():
        self.liters = self.pulse #Put algorithm to calculate liters from pulse

    def getLiters(self):
        return self.liters

    def clearPulse(self):
        self.pulse = 0

getLitersFromDB = [0,0,0,0,0]

firstTap = FlowSensor(FIRST_TAP[POS], FIRST_TAP[GPIO], getLitersFromDB[FIRST_TAP[POS]])
secondTap = FlowSensor(SECOND_TAP[POS], SECOND_TAP[GPIO], getLitersFromDB[SECOND_TAP[POS]])
thirdTap = FlowSensor(THIRD_TAP[POS], THIRD_TAP[GPIO], getLitersFromDB[THIRD_TAP[POS]])
fourthTap = FlowSensor(FOURTH_TAP[POS], FOURTH_TAP[GPIO], getLitersFromDB[FOURTH_TAP[POS]])
fifthTap = FlowSensor(FIFTH_TAP[POS], FIFTH_TAP[GPIO], getLitersFromDB[FIFTH_TAP[POS]])

#GPIO.add_event_detect(PIN, GPIO.RISING, callback=my_callback)
#GPIO.cleanup()
