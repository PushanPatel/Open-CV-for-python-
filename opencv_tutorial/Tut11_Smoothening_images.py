"""
Tutorial 18: Smoothening of images
Smoothing or blurring is used to remove noise from image using filters such as
Homogeneous: most simple. each output pixel is mean of its kernel neighbours
Gaussian
Median
bilateral
etc
Kernel,convultion matrix is a shape which can apply/convolve over image. Used for blurring, sharpening, embossing, edge detection etc

"""

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

#img=cv2.imread('opencv-logo.png')
img=cv2.imread('pic2.png')
#img=cv2.imread('lena.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)# as we are using matplotlib

#for homogeneous, kernel K=1/(Kwidth*Kheight)*(matrix of 1s)
Kh=5
Kw=5
kernel=np.ones((Kh,Kw),np.float32)/(Kh*Kw)
dst=cv2.filter2D(img,-1,kernel)# this destination image
#filter2D(source,depth of dest. image,kernel) filter2D is filter for homogeneous\
# it smooths the curves(noises there are removed)

#For one Dimensional signals of Image- Low Pass Filter and High Pass filters are used
#LPF helps in removing noises and blurring images
#HPF helps in finding edges in image
blur=cv2.blur(img,(5,5)) # uses averaging method to blur
gauss=cv2.GaussianBlur(img,(5,5),sigmaX=0)# gaussian filter uses different weight kernel in both x and y direction
# center has higher weight and edges have less weight
# better than blur. better at removing high frequency noise

med=cv2.medianBlur(img,5)
# Median filter replaces each pixel value with median of its neighbouring pixels.
#  This method is great when dealing with 'salt and pepper' noise( black as well as white spots as noise)
# kernel should be odd number and not 1

bf=cv2.bilateralFilter(img,9,75,75)
#All above filters not only remove noise but also smoothen the edges. In order to preserve the edges(in some case where we require them)Use bilateral filter
#bilateralFilter(source,diameter of each pixel neighbourhood used, sigma color, sigma space )
titles=['Image','2D convolution','Blur','Gaussian Blur','Median','Bilateral filter']
images=[img,dst,blur,gauss,med,bf]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()