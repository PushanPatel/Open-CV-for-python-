"""
Tutorial 27:Template matching using OpenCV
Template matching is amethod of searching and finding a template image inside a larger image
OpenCV has matchtemplate to do that
"""

import cv2
import numpy as np 
img=cv2.imread("messi5.jpg")# main image
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

temp=cv2.imread("messi_face.jpg",0)# template image which we will find in main image
h,w=temp.shape 

#res=cv2.matchTemplate(imgray,temp,cv2.TM_CCOEFF_NORMED)
res=cv2.matchTemplate(imgray,temp,cv2.TM_CCORR_NORMED)
#matchTemplate(main,template,method) various methods are available which can be learnt from opencv doc available online
print(res)# it contains a matrix and the largest number(brightest point)is the point(in main image) which matches with the top left corner of the template
threshold=0.9#0.95 has only one point and 0.9 has 3 points
loc=np.where(res>=threshold)#array of points which are greater than threshold is formed
print(loc)                  #This filters less bright points

for pt in zip(*loc[::-1]):# iterate to distinguish between results filtered after threshold
    #loc[::-1] is used so that pt contains (width, height) and not (height,width)
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),2)
    #Better threshold implies clearer rectangle
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()