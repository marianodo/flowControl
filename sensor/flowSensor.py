import RPi.GPIO as GPIO

class FlowSensor(object):
    def __init__(self,tapPosition, gpio, liters = 0, label = "-"):
        self.liters = liters
        self.pulse = 0
        self.tapPosition = tapPosition
        self.gpio = gpio
        self.label = label
        self.configureGpioSensors()

    def configureGpioSensors(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.gpio, GPIO.FALLING, callback=self.incrementPulse)

    def incrementPulse(self, channel):
        self.pulse += 1
        self.getLiterAmountFromPulse()

    def getLiterAmountFromPulse(self):
        self.liters += self.pulse #Put algorithm to calculate liters from pulse
        self.pulse = 0

    def getLiters(self):
        return self.liters

    def getLabel(self):
        return self.label

    def setLabel(self, newLabel):
        self.label = newLabel

    def clearPulse(self):
        self.pulse = 0

    def __del__(self):
        GPIO.cleanup()       
