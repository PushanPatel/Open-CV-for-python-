"""
Tutorial video 13: Object detection and tracking using HSV
HSV stands for Hue->color components(base pigments)
[Hue range:0-360=>all colors]
    Saturation->amount of color(depth of pigment or hue)(0-100%)
    Value->brightness of color(0-100%)
HSV is used to separate luminescence from color image which makes it easier to work on
luminescence. That is why we use HSV in problems where color description plays an important role
"""

import cv2
import numpy as np 
def nothing(x):
    pass

cap=cv2.VideoCapture(0)# for live video object tracking

cv2.namedWindow("Tracking")
cv2.createTrackbar("LowHue","Tracking",0,255,nothing)
cv2.createTrackbar("LowSat","Tracking",0,255,nothing)
cv2.createTrackbar("LowVal","Tracking",0,255,nothing)
cv2.createTrackbar("UppHue","Tracking",255,255,nothing)
cv2.createTrackbar("UppSat","Tracking",255,255,nothing)
cv2.createTrackbar("UppVal","Tracking",255,255,nothing)

while True:
    _, frame=cap.read()
    
    #uncomment below line for operating on static image and comment above line
    #frame = cv2.imread('smarties.png')
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    """
    #for pre defined values of lower blue and upper blue
    l_b=np.array([97,50,50])#lower blue color , instructor defined these values and later used track bar
    u_b=np.array([130,255,255])#Upper blue
    mask=cv2.inRange(hsv,l_b,u_b) # defines the range from lower bound to upper bound 
    res=cv2.bitwise_and(frame,frame,mask=mask) # here in bitwise and we are providing both same sources and also a mask
    #mask hides everything except mask values are true
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask) # prints white true values and rest black
    cv2.imshow('Result',res) # only blue balls
    """
    #using tracking to get precise lower and upper bounds
    l_h=cv2.getTrackbarPos("LowHue","Tracking")
    l_s=cv2.getTrackbarPos("LowSat","Tracking")
    l_v=cv2.getTrackbarPos("LowVal","Tracking")

    u_h=cv2.getTrackbarPos("UppHue","Tracking")
    u_s=cv2.getTrackbarPos("UppSat","Tracking")
    u_v=cv2.getTrackbarPos("UppVal","Tracking")

    l_b=np.array([l_h,l_s,l_v])#lower bound
    u_b=np.array([u_h,u_s,u_v])#Upper bound defined by track bar
    mask=cv2.inRange(hsv,l_b,u_b) # defines the range from lower bound to upper bound 
    res=cv2.bitwise_and(frame,frame,mask=mask) # here in bitwise and we are providing both same sources and also a mask
    #mask hides everything except mask values are true
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask) # prints white true values and rest black
    cv2.imshow('Result',res) # only l_b to u_b colors displayed



    k=cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
