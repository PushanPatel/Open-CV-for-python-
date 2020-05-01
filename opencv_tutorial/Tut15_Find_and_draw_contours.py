"""
Tutorial 23: Find and draw contours
Contours:the curve joing all the continuous point along the boundary which are having the same color or intensity
They can be used for shape analysis or object detection or object recognition. For better results we use binary image
"""

import cv2
import numpy as np 
img=cv2.imread('opencv-logo.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# we are using canny edge detection to get contour
ret,thresh=cv2.threshold(imgray, 127,255,0)# binary method
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# gives contour as well as hierarchy as output, findContours(threshold output,contour retrieval mode, contour method)
#contours (here) is a python list of all contours in image. Each individual contour is a numpy array of (x,y) coordinates of boundary points of object
# hierarchy contains information of image topology
#print("Number of Contours = "+str(len(contours)))
#print(contours[0])# these are x,y coordinates and joining them we will get contour
cv2.drawContours(img,contours,-1,(0,255,255),3)# draws the contour
#drawContours(file on which to draw,contour,index(-1 to print all),color,thickness)
#index starts from 0 till len(contours)-1
cv2.imshow('Image',img)
cv2.imshow('Image Gray',imgray)
cv2.imshow('Threshold',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()