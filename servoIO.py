import servoTest
from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x41, debug=True)
pwm.setPWMFreq(20)
input = 0

while input != 'Q':


	input = raw_input('Enter int: ')
	for i in range(int(input)):
#		pwm.setPWM(0, 0, int(i))
		servoTest.setServoPulse(0, int(input))
#		time.sleep(0.001)
