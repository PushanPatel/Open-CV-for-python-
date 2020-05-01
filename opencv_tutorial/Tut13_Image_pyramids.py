"""
Tutorial video 21: Image pyramids
Image pyramids are multiscale signal reprsentation in which signal or an image is
subject to repeated smoothening and subsampling. that is images of different resolutions are presented.
This is used when we want to detect face but the size of faces differ
Two types Gaussian pyramid adn Laplacian pyramid
"""

import cv2
import numpy as np 

img= cv2.imread('lena.jpg')

#Gaussian pyramid is repeat filteing and subsampling of image
#two function under this: pyrUp and pyrDown
"""
#Uncomment to see the effects of pyrDown and pyrUp individually
LowResol=cv2.pyrDown(img)# lowers the resolution by 2
lr2=cv2.pyrDown(LowResol)

HiResol=cv2.pyrUp(img)#increases the resolution
lr2tolr1=cv2.pyrUp(lr2)# The resolution once decreased and then increased gives a blur image as compared to original
# here lr2tolr1 is blurrier then lr1(LowResol) eventhough the resolution is same.
#This happens because some of information is lost when resolution is lowered
cv2.imshow("Original",img)
cv2.imshow("pyrDown 1",LowResol)
cv2.imshow("pyrDown 2",lr2)
cv2.imshow("pyrUp",HiResol)
cv2.imshow("pyrUp: pyrDown 2 to pyrDown 1",lr2tolr1)
"""
layer=img.copy()# this makes the copy of image so that the original is not altered
#gp-> gaussian pyramid array
gp=[layer]
height_of_gp=5
for i in range(height_of_gp+1):
   # cv2.imshow('GP Layer:'+str(i),layer)# 0 represent original image
    if i==5:
        break
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    
#Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid 
#and expanded version of its upper level in Gaussian pyramid
# It gives the edges of image in all resolutions
layer=gp[5]#last image in the list
cv2.imshow('Upper level of GP',layer)
lp=[layer]
for i in range(5,0,-1):
    gauss_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gauss_extended)# to find difference between the two
    cv2.imshow(str(i),laplacian)
    lp.append(laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()