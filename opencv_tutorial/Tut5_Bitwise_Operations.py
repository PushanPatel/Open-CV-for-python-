"""
Tutorial video 11: Bitwise Operations (AND,OR,XOR)

"""
import cv2
import numpy as np 

img1=np.zeros((250,500,3),np.uint8)
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=np.zeros((250,500,3),np.uint8)
img2=cv2.rectangle(img2,(250,0),(500,250),(255,255,255),-1)

bitAnd=cv2.bitwise_and(img2,img1) # logically compares the two images considering black as false and white true
bitOr=cv2.bitwise_or(img2,img1)# Logical or
bitXOR=cv2.bitwise_xor(img2,img1)#XOR
bitNot=cv2.bitwise_not(img2)#Not
# Bitwise operations are very useful when working with masks

cv2.imshow("One",img1)
cv2.imshow("Two",img2)
cv2.imshow("bit and",bitAnd)
cv2.imshow('bit Or',bitOr)
cv2.imshow("bit not img2",bitNot)
cv2.imshow('bit XOR',bitXOR)
cv2.waitKey(0)
cv2.destroyAllWindows() 