"""
Tutorial 26: Understanding histograms in openCV
Histograms are plots that give an idea of intensity distribution of an image
Using histograms you can get information about brightness, intensity,etc of an image
"""
import numpy as np 
import cv2 
from matplotlib import pyplot as plt 

img=np.zeros((200,200),np.uint8)#Total 200x200 pixels
cv2.rectangle(img,(0,100),(100,200),(255),-1)
cv2.rectangle(img,(100,100),(200,200),(127),-1)
cv2.rectangle(img,(100,100),(150,150),(27),-1)
cv2.imshow("Image",img)#Half black,1/4white,1/4 grey

#Histograms can be found using various methods
#Finding histogram using matplotloib
plt.hist(img.ravel(),256,[0,256])
#hist(x,max number of pixels,range of pixel value)
plt.title("Frame: Width x Height-> "+str(img.shape[0])+" x "+str(img.shape[1])+"\nTotal Pixels: "+str(img.shape[0]*img.shape[1]))
plt.show()# y axis shows total number of pixels, x axis is pixel value corresponding to

"""
For a Gray scale image(complexity greater than that of rectangular image above)
"""

img=cv2.imread('lena.jpg',0)
cv2.imshow("Image 2",img)
plt.hist(img.ravel(),256,[0,256])
plt.title("Frame: Width x Height->"+str(img.shape[0])+" x "+str(img.shape[1])+"\nTotal Pixels: "+str(img.shape[0]*img.shape[1]))
plt.show()

"""
For color images BGR
"""
img=cv2.imread('lena.jpg')
b,g,r=cv2.split(img)
List=["Image","Blue","Green","Red"]
Val=[cv2.cvtColor(img,cv2.COLOR_BGR2RGB),b,g,r]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(Val[i],'gray')
    plt.title(List[i])
    plt.xticks([]),plt.yticks([])
plt.show()

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()

#Another method to calculate histogram
img=cv2.imread('lena.jpg',0)
hist=cv2.calcHist([img],[0],None,[256],[0,256])

"""
img=cv2.imread(lena.jpg)
hist=cv2.calcHist([img],[0,1,2],None,[256,256,256],[0,256])
#calcHist([source],[channel indexes which are to be considered],mask,hist size,range of value)
"""
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()