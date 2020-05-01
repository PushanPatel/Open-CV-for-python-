"""
Tutorial video 12: bind track bars to opencv
Track bars are used to change values dynamically at runtime
"""

import cv2
import numpy as np 

def nothing(x): #x is the value returned by trackbar when it is changed
    print(x)
#creating a black image and window
img=np.zeros((300,500,3),np.uint8)
cv2.namedWindow('image')# to create a window with a name 'image'

#creating trackbars to adjust B,G,R values
#multiple track bars can be created so a name is required for it
cv2.createTrackbar('B','image',0,255,nothing)
#createTrackbar('name',windowname,initial value,final value or count,callback function or Onchange)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

#For second example:
#img2=np.zeros((300,500,3),np.uint8)
 
cv2.namedWindow('img2')

sw2='color/gray'
cv2.createTrackbar(sw2,'img2',0,1,nothing)
cv2.createTrackbar('CP','img2',10,400,nothing)


while(1):
   
    img2=cv2.imread('messi5.jpg',1)# reads everytime so that new text appears and old disappears
    cv2.imshow('image',img)# called the window 'image'
    
    k=cv2.waitKey(1) & 0xFF
    if k== ord('q'):
        break
    b=cv2.getTrackbarPos('B','image') # returns the current position of corresponding trackbar
    g=cv2.getTrackbarPos('G','image')
    r=cv2.getTrackbarPos('R','image')
    s=cv2.getTrackbarPos(switch,'image')
    if s==1: # if switch is On only then there will be a change else remain as it was before switched OFF
        img[:]=[b,g,r] # assigns b,g,r value to all the pixel points

    s2=cv2.getTrackbarPos(sw2,'img2')
    strPos=str(cv2.getTrackbarPos('CP','img2'))
    font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(img2,strPos,(250,150), font,4,(b,g,r),3)
    
    if s2==0:#Color mode
        pass
    else:#gray mode
        img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    cv2.imshow('img2',img2)
cv2.destroyAllWindows()
