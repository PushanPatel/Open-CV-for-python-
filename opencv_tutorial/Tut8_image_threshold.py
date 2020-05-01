"""
Tutorial 14: Simple Image thresholding
separating pixels based on threshold value set(higher intensity in one group oand rest in other)
We can then assign different values to each group
in simple thresholding we compare using a global value which is same for all
Here we are employing thresholding to gray scale images.
To do for color or hsv images use split and then apply thresholding according to need.
 Like in HSV we can use thresholding to keep brightness to a certain level
"""
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img=cv2.imread('gradient.png',0)# it is better to give file path to avoid any errors. Here we are using file name
_, th1=cv2.threshold(img,90,255,cv2.THRESH_BINARY)# threshold(variable, threshold value, max value, thresholding type) here type is binary
# in binary threshold : values less than threshold are 0 and rest 255
# this function returns two values : one is ret=true or false which we dont want right now and other is threshold
_, th2=cv2.threshold(img,90,255,cv2.THRESH_BINARY_INV)
# binary inverse gives 0 to intensities higher than threshold
_, th3=cv2.threshold(img,90,255,cv2.THRESH_TRUNC)
#Trunc keeps the intensities same as original till threshold and rest are assigned the intensities equal to threshold
_, th4=cv2.threshold(img,90,255,cv2.THRESH_TOZERO)
# To_zero: assigns 0 to pixel values less then threshold rest same as original 
_, th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#assignes 0 to pixel values higher than threshold and rest same as original
_, th6=cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#Automatically takes the threshold value

# to plot together using mayplotlib: learnt from website while searching about thresholding
titles=['Gradient Original','Binary','Binary inverse','trunc','ToZero','To Zero inverse','Otsu']
images=[img,th1,th2,th3,th4,th5,th6]

for i in range(7):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray') # if gray is not mentioned than it will be a bit colored graph
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""
cv2.imshow('Image',img)
cv2.imshow('Th1-Binary Threshold',th1)
cv2.imshow('Th2 - Binary threshold inverse',th2) 
cv2.imshow('Th3 - Trunc ',th3)
cv2.imshow('Th4 - Tozero',th4)
cv2.imshow('Th5 - To zero inverse',th5)
"""

"""
Tutorial video 15: Adaptive thresholding
Thresholding is calculated for a smaller region. Therefore different regions have different threshold
"""
img2=cv2.imread('sudoku.png',0)
_,th= cv2.threshold(img2,127,255,cv2.THRESH_BINARY)# to show limitations of simple thresholding

ath1=cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,4)
# adaptiveThreshold(source,maxvalue,adaptive method,threshold type,block size, constant that will be deducted from mean)
# more the constant is increased less disturbances(black spots) appear
ath2=cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,4)
# works on gaussian mean methods rather tha normal mean. more cleared black spots
_,th_o=cv2.threshold(img2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Original',img2)
cv2.imshow('Problem pic',th)
cv2.imshow('Adaptive -> Thresh mean c',ath1)
cv2.imshow('Adaptive -> Gaussian c',ath2)
cv2.imshow('Otsu for this',th_o)


cv2.waitKey(0)
cv2.destroyAllWindows()