import cv2
import cv2.cv as cv
import numpy as np

kernel = np.ones((5,5),np.uint8)

cap = cv2.VideoCapture(0)

while(1):
	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([0, 100, 100])
	upper_blue = np.array([255, 140, 140])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	tracking = cv2.bitwise_and(hsv, lower_blue, upper_blue)


	dilation = cv2.dilate(tracking,kernel,iterations = 1)
   	closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
	closing = cv2.GaussianBlur(closing,(5,5),0)

	# Detect circles using HoughCircles
	circles = cv2.HoughCircles(closing,cv.CV_HOUGH_GRADIENT,2,120,param1=120,param2=50,minRadius=10,maxRadius=0)
	# circles = np.uint16(np.around(circles))

	#Draw Circles
	if circles is not None:
		for i in circles[0,:]:
                # If the ball is far, draw it in green
	                if int(round(i[2])) < 30:
				cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,255,0),5)
				cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,255,0),10)
			# else draw it in red
        	        elif int(round(i[2])) > 35:
                	    	cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,0,255),5)
                    		cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,0,255),10)
                    		buzz = 1

	#you can use the 'buzz' variable as a trigger to switch some GPIO lines on Rpi :)
    # print buzz                    
    # if buzz:
        # put your GPIO line here

    
    #Show the result in frames
	cv2.imshow('HueComp',hthresh)
	cv2.imshow('SatComp',sthresh)
	cv2.imshow('ValComp',vthresh)
	cv2.imshow('closing',closing)
	cv2.imshow('tracking',frame)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()

cv2.destroyAllWindows()
