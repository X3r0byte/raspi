import servoTest
import os
import sched
import us
import threading
import time
import motorTest
import cv2
import cv2.cv as cv
import numpy as np
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x41)
pwm.setPWMFreq(20)

servoPos = 64
flag2 = 0
flag = 0
servoTest.setServoPulse(0, servoPos)

kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
cap.set(3, 160)
cap.set(4, 120)

def getX(closing):
    M = cv2.moments(closing)
    if int(M['m00']) is not 0:
        if int(M['m00']) > 8000:
            centroid_x = int(M['m10']/M['m00'])
#            print("X Value: " + str(centroid_x))
	    return centroid_x
    return -1		

def getY(closing):
    M = cv2.moments(closing)
    if int(M['m00']) is not 0:
        centroid_y = int(M['m01']/M['m00'])
#        print("Y Value: " + str(centroid_y))
	return centroid_y

def getArea(closing):
    M = cv2.moments(closing)
    return M['m00']

def scan():
    global servoPos
    global flag
    if flag != 1:
        servoPos = servoPos+1
	servoTest.setServoPulse(0, servoPos)
	if servoPos > 80:
            flag = 1
    elif flag != 0:
	servoPos = servoPos-1
	servoTest.setServoPulse(0, servoPos)
	if servoPos < 42:
	    flag = 0
    else:
	pass


def look(x):

    global servoPos
    if servoPos > 0 and servoPos < 1000:
        if x < 70 and x > 30:
            servoPos = servoPos-1
            servoTest.setServoPulse(0, servoPos)        
        elif x > 90 and x < 130:
	    servoPos = servoPos+1
	    servoTest.setServoPulse(0, servoPos)
        elif x <= 30 and x > 1:
	    servoPos = servoPos-3
	    servoTest.setServoPulse(0, servoPos)
        elif x >= 130 and x < 160:
	    servoPos = servoPos+3
	    servoTest.setServoPulse(0, servoPos)
	else:
	    pass


def findColor(x, y, area):
    global flag2
    global servoPos
    if area < 50:
        flag2 = 0

    if x > 1 and y > 1 and area > 5000: #was 5000

	print("*** X is: " + str(x) + "*** Y is: " + str(y))
        point = (x, y)

#	print("AREA OF COLOR IS: "+ str(area))
#        cv2.circle(frame, point, 10, (255,0,0), 0)
#        if x < 70 and y < 75:
#            motorTest.forward(50, 220-x)
#        elif x > 90 and y < 75:
#            motorTest.forward(70+x, 50)
#        elif x > 70 and x < 90 and y < 75:
#            motorTest.forward(250, 250)

	if servoPos < 60:
	    motorTest.forward(50, 200)
	elif servoPos > 68:
	    motorTest.forward(200, 50)
	else:
	    motorTest.forward(200, 200)

        if y > 175 or area > 15000:
	    motorTest.off()
	    if flag2 == 0:
	        os.system('mpg123 -f 57000 -m clip.mp3 &')
	        flag2 = 1

#        elif y > 95 and y < 150:
#	    motorTest.reverse(180)
#            time.sleep(0.3)
#        elif x <= 1 and y <= 1 or area < 6500:
#	motorTest.forward(250, 250)
#            motorTest.off() 

def navigate():

    rangeL = us.rangeL()
    rangeR = us.rangeR()

    if rangeL < 20 and rangeL > 8 or rangeL < 6:
        motorTest.avoidReverseL()

    elif rangeR < 20 and rangeR > 8 or rangeR < 6:
        motorTest.avoidReverseR()

    if rangeL < 100 or rangeR < 100:
        if rangeL - rangeR > 12:
            motorTest.forward(75, 290)

        elif rangeL - rangeR < -12:
            motorTest.forward(290, 75)
    else:
	motorTest.forward(275, 275)


def nothing(x):
    pass

def filter():
#    cv2.namedWindow('HueComp')
#    cv2.namedWindow('SatComp')
#    cv2.namedWindow('ValComp')
#    cv2.namedWindow('closing')
    cv2.namedWindow('tracking')
# Creating track bar for min and max for hue, saturation and value
#    cv2.createTrackbar('hmin', 'HueComp',43,179,nothing)
#    cv2.createTrackbar('hmax', 'HueComp',74,179,nothing)

#    cv2.createTrackbar('smin', 'SatComp',45,255,nothing)
#    cv2.createTrackbar('smax', 'SatComp',147,255,nothing)

#    cv2.createTrackbar('vmin', 'ValComp',135,255,nothing)
#    cv2.createTrackbar('vmax', 'ValComp',199,255,nothing)

def showFrames():
#    cv2.imshow('HueComp', hthresh)
#    cv2.imshow('SatComp', sthresh)
#    cv2.imshow('ValComp', vthresh)
#    cv2.imshow('closing', closing)
    cv2.imshow('tracking', frame)

def getColor(color):
    value = []
    if color == 2:
        value.append(0)
        value.append(0)
        value.append(0)
        value.append(0)
        value.append(0)
        value.append(0)

    else:	
        value.append(43)
        value.append(74)
        value.append(45)
        value.append(147)
        value.append(135)
        value.append(199)

    return value

#filter()

#cv2.namedWindow('closing')
cv2.namedWindow('tracking')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#===================== RUNTIME LOOP ========================================
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

while(1):
    values = getColor(1)
    buzz = 0
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    b,g,r = cv2.split(hsv)

    hmn = values[0]
    hmx = values[1]
    smn = values[2]
    smx = values[3]
    vmn = values[4]
    vmx = values[5]

#    hmn = cv2.getTrackbarPos('hmin','HueComp')
#    hmx = cv2.getTrackbarPos('hmax','HueComp')
#    smn = cv2.getTrackbarPos('smin','SatComp')
#    smx = cv2.getTrackbarPos('smax','SatComp')
#    vmn = cv2.getTrackbarPos('vmin','ValComp')
#    vmx = cv2.getTrackbarPos('vmax','ValComp')


#====================================================================
#-----------------   IMAGE PROCESSING   -----------------------------
#=====================================================================


    hthresh = cv2.inRange(np.array(b),np.array(hmn),np.array(hmx))
    sthresh = cv2.inRange(np.array(g),np.array(smn),np.array(smx))
    vthresh = cv2.inRange(np.array(r),np.array(vmn),np.array(vmx))
    # AND h s and v
    tracking = cv2.bitwise_and(hthresh,cv2.bitwise_and(sthresh,vthresh))
    # Some morpholigical filtering
    dilation = cv2.dilate(tracking,kernel,iterations = 1)
    closing = dilation
#    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
#    closing = cv2.GaussianBlur(closing,(5,5),0)


#=================================================================
#-----------------------  LOGICAL PROCESSING  ------------------
#=================================================================
    x = getX(closing)
    y = getY(closing)
    area = (getArea(closing)/100)
    
#    navigate()
    look(x)
    if area > 500:
	findColor(x, y, area)

    showFrames()

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
