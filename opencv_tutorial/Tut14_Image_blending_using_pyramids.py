"""
Tutorial 22: Image blending using Pyramids

"""

import cv2
import numpy as np 

apple=cv2.imread('apple.jpg')
orange=cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)

apple_orange=np.hstack((apple[:,:256],orange[:,256:]))#Left apple right orange
cv2.imshow('Apple_Orange',apple_orange)#We can see the line which divides both
#that is why image blending is required. 5 steps for blending using pyramids
#1. Load the two images. 2.Find gaussian pyramids for both(in this example levels=6)
#3. From gaussian find lapalcian pyramid. 4 Join the left half of apple and right of orange in each level
#5.Finally from this joint image pyramids, reconstruct original

#Gaussian P of apple
apple_copy=apple.copy()
gp_apple=[apple_copy]

for i in range(5):# 6 Layers( original(0 level) included)
    apple_copy=cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#Gaussian P of orange
orange_copy=orange.copy()
gp_orange=[orange_copy]

for i in range(5):# 6 Layers( original(0 level)included)
    orange_copy=cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#Laplacian of Apple
lp_apple=[gp_apple[5]]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp_apple[i])
    laplacian=cv2.subtract(gp_apple[i-1],gaussian_extended)
    lp_apple.append(laplacian)

#Laplacian of Orange
lp_orange=[gp_orange[5]]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp_orange[i])
    laplacian=cv2.subtract(gp_orange[i-1],gaussian_extended)
    lp_orange.append(laplacian)

#Now add left apple and right orange halves
apple_orange_pyramid=[]

for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    cols,rows,ch=apple_lap.shape
    laplacian=np.hstack((apple_lap[:,0:int(cols/2)],orange_lap[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#Now reconstruct
apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)

gauss=cv2.GaussianBlur(apple_orange_reconstruct,(5,5),sigmaX=0)# just like that
cv2.imshow('Apple_orange Blended',apple_orange_reconstruct)
cv2.imshow('Apple',apple)
cv2.imshow('Blended and then gauss blur',gauss)
cv2.imshow("orange",orange)
cv2.waitKey(0)
cv2.destroyAllWindows()
