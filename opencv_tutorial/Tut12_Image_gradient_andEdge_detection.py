"""
19,20
Tutorial 19: Image gradient and edge detection
Image gradient is a directional change in the intensity or color in an image
Three method: laplacian derivative, sobelx, sobely
Sobel method is joint gaussian and differentiation methods
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt 

#img=cv2.imread('messi5.jpg',0)
img=cv2.imread('lena.jpg',0)
#img=cv2.imread('messi5.jpg',1)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#img=cv2.imread('sudoku.png',0)# for a better understanding

lap=cv2.Laplacian(img,cv2.CV_64F, ksize=3)
#Laplacian(source,dataType, kernel size)
#we are using 64F datatype(64 bit float) due to the negative slope induced by transforming
# the image from white to black. So this data type supports negative numbers which we will be dealing with
# when laplacian method is used
# in this case the image detoriates as we increase kernel size. By default it takes 1 which gives clear outline of messi
lap=np.uint8(np.absolute(lap))
#converted from 64F to uint8 because this is suitable to output

#Sobelx and sobely are known as sobel gradients
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0,2) # works along vertical direction
#Sobel(img, cv2.CV_64F,Derivative index/order of X,derivative index of y,kernel size(defalut 1))
sobelX=np.uint8(np.absolute(sobelX))

sobelY=cv2.Sobel(img,cv2.CV_64F,0,1,2)#works along horizontal direction
sobelY=np.uint8(np.absolute(sobelY))

sobelCombined=cv2.bitwise_or(sobelX,sobelY)# for combined effect. Much better than individual
sobelXY=cv2.Sobel(img,cv2.CV_64F,1,1)#I am trying to get order of differentiation for bot x and y
sobelXY=np.uint8(np.absolute(sobelXY))


"""
Tutorial video 20: Canny edge detection
It is an iedge detection operator that uses multistage alogorithm to detect a wide range of edges in images
5 steps:
1. Noise reduction: by gaussian filter
2.Gradient calculation
3.Non maximum suppression to get rid of spurious response to edge dection
4.Double threshold to determine potential edges
5.Edge tracking by hysterisis

"""
canny=cv2.Canny(img,100,200)
#All the steps are carried easily by Canny function
#Canny(source,threshold1,threshold2,)
# can use trackbars to get appropriate values of threshold
# better and clearer results then other gradients

titles=['image','Laplacian','Sobel X','Sobel Y','Sobel combined','Sobel XY','Canny edge detection']
images=[img,lap,sobelX,sobelY,sobelCombined,sobelXY,canny]

for i in range(7):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

