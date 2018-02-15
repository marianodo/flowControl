
import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)
PIN = 4
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

contador = 0

def my_callback(channel):
    global contador
    contador += 1
    import sys
    #acter
    sys.stdout.write('%d' % contador)
    sys.stdout.flush()
    i=1
    while i<=len(str(contador)):
        sys.stdout.write('\b')
        i = i+1;

GPIO.add_event_detect(PIN, GPIO.RISING, callback=my_callback)

raw_input("Press Enter Para salir del programa \n")
GPIO.cleanup()
