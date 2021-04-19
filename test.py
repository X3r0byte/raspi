from SimpleCV import *
import cv2
import numpy as np

cap = cv2.VideoCapture(0)


cap.set(3, 160)
cap.set(4, 120)

while(1):

	var, img = cap.read()
	simpleCVimg = Image(img)

	_, frame = cap.read()


	

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,355,355])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	res = cv2.bitwise_and(frame, frame, mask= mask)

	cv2.imshow('frame', frame)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
