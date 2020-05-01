"""
Tutorial video 8: handle mouse events
"""

import cv2
import numpy as np
""" 
events = [i for i in dir(cv2) if 'EVENT' in i] # to print all events in cv2 library 
print(events)
#['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON',
 #'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 
 #'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 
 #'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
"""
def click_event(event, x, y,flags,param):
    if event ==cv2.EVENT_LBUTTONDOWN: # means left button is pressed and up means released
      #  print(x,', ',y)          # refer this link for mouse event meanings: https://docs.rs/opencv/0.23.0/opencv/highgui/constant.EVENT_LBUTTONDOWN.html
        font=cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x)+', '+str(y)
        cv2.putText(img,strXY,(x,y),font,0.3,(0,255,0),1)
        cv2.imshow('image',img)
    
    elif event==cv2.EVENT_RBUTTONDOWN:#following is to print RGB of point
        blue=img[y,x,0] #returns the blue conc at x,y coordinate the list is height,width,list of BGR resp. conc.
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_DUPLEX
        strXY=str(red)+', '+str(green)+', '+str(blue)
        cv2.putText(img,strXY,(x,y),font,0.3,(200,255,0),1)
        cv2.imshow('image',img)

"""
Tutorial video 9: more mouse events
"""


x1=None
y1=None
def click_event2(event,x,y,flag,param):#for tutorial 9-> draw line joining two points
    global x1
    global y1
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(0,255,0),2)
        cv2.imshow('image',img)
    elif event==cv2.EVENT_RBUTTONDOWN:# this below is completely written by me
        cv2.circle(img,(x,y),3,(0,0,255),2,cv2.LINE_AA)
        if x1==None:
            x1=x
            y1=y
        else:
            cv2.arrowedLine(img,(x1,y1),(x,y),(200,255,0),3)
            x1=None
        cv2.imshow('image',img)
    elif event==cv2.EVENT_MBUTTONDOWN: #to display the color of point u have double clicked
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        color=np.zeros((512,512,3),np.uint8)
        color[:]=[b,g,r]
        cv2.imshow('color',color)
        print('Y')
points=[]
img=cv2.imread('Lena.jpg',1)
cv2.imshow('image',img) #keep the window name same
#cv2.setMouseCallback('image',click_event)
# returns the event,coordinates of mouse, flags and param
cv2.setMouseCallback('image',click_event2)#for tutorial video 9
cv2.waitKey(0)
cv2.destroyAllWindows()


