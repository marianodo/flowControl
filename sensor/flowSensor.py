import RPi.GPIO as GPIO

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

    def __del__(self):
        GPIO.cleanup()       
