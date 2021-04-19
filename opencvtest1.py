import us
import threading
import time
import motorTest
import cv2
import cv2.cv as cv
import numpy as np

kernel = np.ones((5,5),np.uint8)
# Take input from webcam
cap = cv2.VideoCapture(0)

# Reduce the size of video to 320x240 so rpi can process faster; 3320 and 4240
# Window Parameters 
cap.set(3, 160)
cap.set(4, 120)


def discovery():
    motorTest.turnRight()
    time.sleep(0.3)
    motorTest.forward(150, 150)
#    time.sleep(0.3)
    motorTest.turnLeft()
#    time.sleep(0.3)
#    motorTest.rev()
    time.sleep(0.002)



# returns x coordinate of color if the object area is greater than 10000
def getX(closing):
    M = cv2.moments(closing)
    if int(M['m00']) is not 0:
        if int(M['m00']) > 8000:
            centroid_x = int(M['m10']/M['m00'])
            print("X Value: " + str(centroid_x))
	    return centroid_x
    return -1		

# returns y coordinate of color
def getY(closing):
    M = cv2.moments(closing)
    if int(M['m00']) is not 0:
        centroid_y = int(M['m01']/M['m00'])
        print("Y Value: " + str(centroid_y))
#	print("AREA AREA AREA ********:   " + str(M['m00']) + "     : ***********")
	return centroid_y

def findColor(x, y):
	
    if x > 1 and y > 1:
        point = (x, y)
        cv2.circle(frame, point, 10, (255,0,0), 0)
        if x < 70 and y < 75:
            motorTest.forward(50, 220-x)
            print("Color is to the left. Offset of: " + str(220-x) + " speed.")
        elif x > 90 and y < 75:
            motorTest.forward(70+x, 50)
            print("Color is to the right. Offset of: " + str(70+x) + " speed.")
        elif x > 70 and x < 90 and y < 75:
            motorTest.forward(250, 250)
            print("Color is in center")
        if y > 75 and y < 95:
	    motorTest.off()
            time.sleep(0.1)
        elif y > 95 and y < 150:
	    motorTest.reverse(180)
            time.sleep(0.3)
    elif x <= 1 and y <= 1:
        motorTest.off()

def nothing(x):
    pass

# Creating a windows for later use
cv2.namedWindow('HueComp')
cv2.namedWindow('SatComp')
cv2.namedWindow('ValComp')
cv2.namedWindow('closing')
cv2.namedWindow('tracking')


# Creating track bar for min and max for hue, saturation and value
# You can adjust the defaults as you like
cv2.createTrackbar('hmin', 'HueComp',43,179,nothing)
cv2.createTrackbar('hmax', 'HueComp',74,179,nothing)

cv2.createTrackbar('smin', 'SatComp',45,255,nothing)
cv2.createTrackbar('smax', 'SatComp',147,255,nothing)

cv2.createTrackbar('vmin', 'ValComp',135,255,nothing)
cv2.createTrackbar('vmax', 'ValComp',199,255,nothing)


while(1):

    buzz = 0
    _, frame = cap.read()

    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	
    b,g,r = cv2.split(hsv)
#    hsv = cv2.merge([r,g,b])

    # get info from track bar and appy to result
    hmn = cv2.getTrackbarPos('hmin','HueComp')
    hmx = cv2.getTrackbarPos('hmax','HueComp')
    

    smn = cv2.getTrackbarPos('smin','SatComp')
    smx = cv2.getTrackbarPos('smax','SatComp')


    vmn = cv2.getTrackbarPos('vmin','ValComp')
    vmx = cv2.getTrackbarPos('vmax','ValComp')

    # Apply thresholding
    hthresh = cv2.inRange(np.array(b),np.array(hmn),np.array(hmx))
    sthresh = cv2.inRange(np.array(g),np.array(smn),np.array(smx))
    vthresh = cv2.inRange(np.array(r),np.array(vmn),np.array(vmx))

    # AND h s and v
    tracking = cv2.bitwise_and(hthresh,cv2.bitwise_and(sthresh,vthresh))

    # Some morpholigical filtering
    dilation = cv2.dilate(tracking,kernel,iterations = 1)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
#    closing = cv2.GaussianBlur(closing,(5,5),0)

#    findCircles(closing)
    x = getX(closing)
    y = getY(closing)  

    findColor(x, y)

    if y > 75:
         motorTest.off()

    

    print us.range()

    #Show the result in frames
#    cv2.imshow('HueComp',hthresh)
#    cv2.imshow('SatComp',sthresh)
#    cv2.imshow('ValComp',vthresh)
    cv2.imshow('closing',closing)
    cv2.imshow('tracking',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
