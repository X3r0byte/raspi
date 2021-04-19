from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import random


mh = Adafruit_MotorHAT(addr=0x60)

motorL = mh.getMotor(3)
motorR = mh.getMotor(1)
speed = 0
num = 0



def off():
	motorL.run(Adafruit_MotorHAT.RELEASE)
	motorR.run(Adafruit_MotorHAT.RELEASE)


def spin():
	print "Celebrate!"
	motorL.run(Adafruit_MotorHAT.FORWARD)
	motorR.run(Adafruit_MotorHAT.BACKWARD)
	motorL.setSpeed(250)
	motorR.setSpeed(250)
	time.sleep(2)



def avoidReverseL():
#        print "Avoiding in Reverse..."
	randNum = random.randint(7, 9)
	randTime = float((randNum/10))

        motorL.run(Adafruit_MotorHAT.BACKWARD)
        motorR.run(Adafruit_MotorHAT.BACKWARD)
        motorL.setSpeed(150)
        motorR.setSpeed(275)
        time.sleep(0.1)
        motorL.run(Adafruit_MotorHAT.FORWARD)
        motorL.setSpeed(250)
        motorR.setSpeed(250)
        time.sleep(0.3)


def avoidReverseR():
#	print "Avoiding in Reverse..."
  	randNum = random.randint(7, 9)
        randTime = float((randNum/10))

	motorL.run(Adafruit_MotorHAT.BACKWARD)
	motorR.run(Adafruit_MotorHAT.BACKWARD)
	motorL.setSpeed(275)
	motorR.setSpeed(150)
	time.sleep(0.1)
	motorR.run(Adafruit_MotorHAT.FORWARD)
	motorL.setSpeed(250)
	motorR.setSpeed(250)
	time.sleep(0.3)



def forward(leftSpeed, rightSpeed):
	if leftSpeed > 0 and rightSpeed > 0:
		motorL.run(Adafruit_MotorHAT.FORWARD)
		motorR.run(Adafruit_MotorHAT.FORWARD)
#		print "Going Forward..."
		motorL.setSpeed(leftSpeed)
		motorR.setSpeed(rightSpeed)








def reverse(object):
        if object > 0:
                if object < 220:
                        motorL.run(Adafruit_MotorHAT.BACKWARD)
                        motorR.run(Adafruit_MotorHAT.BACKWARD)
#                        print "Going in Reverse..."
                        motorL.setSpeed(object)
                        motorR.setSpeed(object)
        else:
                print("Invalid speed: ", object)


def turnRight():
        motorL.run(Adafruit_MotorHAT.FORWARD)
        motorR.run(Adafruit_MotorHAT.BACKWARD)
#        print "exec right turn..."
        for i in range(250):
                motorL.setSpeed(i)
                motorR.setSpeed(i/2)
                time.sleep(0.005)
        motorL.run(Adafruit_MotorHAT.RELEASE)
        motorR.run(Adafruit_MotorHAT.RELEASE)


def turnLeft():
        motorL.run(Adafruit_MotorHAT.BACKWARD)
        motorR.run(Adafruit_MotorHAT.FORWARD)
#        print "exec left turn..."
        for i in range(250):
                motorL.setSpeed(i/2)
                motorR.setSpeed(i)
                time.sleep(0.005)
        motorL.run(Adafruit_MotorHAT.RELEASE)
        motorR.run(Adafruit_MotorHAT.RELEASE)

def creep(object):
	if object <= 250:
	        motorL.run(Adafruit_MotorHAT.FORWARD)
	        motorR.run(Adafruit_MotorHAT.FORWARD)
#	        print "exec creep forward..."
	        for i in range(object):
			print ('.' * i)
        	        motorL.setSpeed(i)
        	        motorR.setSpeed(i)
        	        time.sleep(0.01)
		time.sleep(2.5)
		for i in reversed(range(object)):
			print ('.' * i)
			motorL.setSpeed(i)
			motorR.setSpeed(i)
			time.sleep(0.01)
        	motorL.run(Adafruit_MotorHAT.RELEASE)
        	motorR.run(Adafruit_MotorHAT.RELEASE)
	else:
		print "She can't take that kind of load, captain!"

def randomForward():
	speed = random.randint(25, 100)
        motorL.run(Adafruit_MotorHAT.FORWARD)
        motorR.run(Adafruit_MotorHAT.FORWARD)
        print "exec Forward at random speed..."
        for i in range(speed):
		print i
                motorL.setSpeed(i)
                motorR.setSpeed(i)
                time.sleep(0.005)
	print('Current speed is: ' + str(speed) + ' RPMs')
	time.sleep(4)
	for i in reversed(range(speed)):
		print i
		motorL.setSpeed(i)
		motorR.setSpeed(i)
		time.sleep(0.01)
        motorL.run(Adafruit_MotorHAT.RELEASE)
        motorR.run(Adafruit_MotorHAT.RELEASE)
