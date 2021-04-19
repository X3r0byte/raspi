import motorTest

direction = ''
speed = 10
ans = ''

while direction != 'Q':
	direction = raw_input('Enter (F)orward, (B)ackward, (L)eft, (R)ight, (C)reep, (V)ariable random, or (Q)uit: ')
	if direction == 'B':
		motorTest.reverse()
	elif direction == 'F':
		motorTest.forward()
	elif direction == 'L':
		motorTest.turnLeft()
	elif direction == 'R':
		motorTest.turnRight()
	elif direction == 'C':
		speed = raw_input('Enter desired RPM: ')
		motorTest.creep(int(speed))
	elif direction == 'V':
		motorTest.randomForward()
	else:
		print('Incorrect input. Answer better. ')
