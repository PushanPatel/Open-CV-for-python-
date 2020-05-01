"""
Tutorial 24: Motion detection and tracking

"""
import cv2
import numpy as np 

cap=cv2.VideoCapture('vtest.avi')
fps=cap.get(cv2.CAP_PROP_FPS)
#print(fps)

ret, frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    """
    # basic contours drawing-> this gets the moving humans but also considers the white line(footpath line) people hide and show when moving. No rectangles around people which we want 
    diff=cv2.absdiff(frame1,frame2)# for absolute difference unlike subtract
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)#better contours in gray scale
    gblur=cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh=cv2.threshold(gblur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)# to fill in all the holes to get better contours. Kernel here is given None
    contours,hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    """
    # Better contour with rejecting unwanted cases
    diff=cv2.absdiff(frame1,frame2)# for absolute difference unlike subtract
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)#better contours in gray scale
    gblur=cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh=cv2.threshold(gblur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)# to fill in all the holes to get better contours. Kernel here is given None
    contours,hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #Iterate over contours to get desired results
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)# x,y coordinate of top corner and width and height of it
        # we will find area and compare based on are we require(like that by a human or a dog and not small enough to consider strap's white dashes)
        if cv2.contourArea(contour)<900:# larger the area less disturbances but decreases precision of detection as well
            continue#didnt draw rectangle for this one
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Status: {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        #cv2.drawContours(frame1,contour,-1,(0,255,0),2)
        #Rectangles gives better representation
    cv2.imshow('Inter',frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv2.waitKey(int(1000/fps))==ord('q'):#1000/fps ms because the frames were taken at some frame rate
        break                           # can reduce delay time to speed up the video
cv2.destroyAllWindows()
cap.release


