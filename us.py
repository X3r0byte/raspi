import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


def rangeR():

	signalon = None
	signaloff = None
	GPIO.setup(17, GPIO.OUT)
        GPIO.setup(4,GPIO.IN)
        GPIO.output(17, GPIO.LOW)

	time.sleep(0.005)
	GPIO.output(17, True)
	time.sleep(0.00001)
	GPIO.output(17, False)

       	while GPIO.input(4) == 0:
		signaloff = time.time()
	while GPIO.input(4) == 1:
		signalon = time.time()

	if signalon is not None and signaloff is not None:
		timepassed = signalon - signaloff
        	distance = timepassed * 17000
	else:
		distance = 1*17000
        return distance

	GPIO.cleanup()

def rangeL():

        signalon = None
        signaloff = None
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22,GPIO.IN)
        GPIO.output(27, GPIO.LOW)

        time.sleep(0.005)
        GPIO.output(27, True)
        time.sleep(0.00001)
        GPIO.output(27, False)

        while GPIO.input(22) == 0:
                signaloff = time.time()
        while GPIO.input(22) == 1:
                signalon = time.time()

        if signalon is not None and signaloff is not None:
                timepassed = signalon - signaloff
                distance = timepassed * 17000
        else:
                distance = 1*17000
        return distance

        GPIO.cleanup()

