from SimpleCV import *
import cv2
import numpy as np

cap = cv2.VideoCapture(0)


cap.set(3, 160)
cap.set(4, 120)


def rotate(cvImg):
        (h, w) = cvImg.shape[:2]
        center = (w / 2, h / 2)
        m = cv2.getRotationMatrix2D(center, 270, 1.0)
        rotated = cv2.warpAffine(cvImg, m, (w,h))
	return rotated



while(1):

	var, img = cap.read()
	simpleCVimg = Image(img)




	green_stuff = simpleCVimg.colorDistance(Color.GREEN)
	green_blobs = green_stuff.findBlobs()
	print("Green detected at X: " + str(green_blobs[-1].x) + ", Y:" + str(green_blobs[-1].y))





	simpleCVimg2 = simpleCVimg.scale(2)
	cvImg = simpleCVimg2.getNumpy()
	finImg = rotate(cvImg)
	cv2.imshow('cvImg', finImg)	

	

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
