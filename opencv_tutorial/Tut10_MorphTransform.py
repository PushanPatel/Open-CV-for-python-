"""
Tutorial vidoe 17: Morphological Transformation

Morphological transformations are some simple operations based on the image shape. Normally performed on binary images.
Two things required the image and structuring element called kernel which decides nature of operation
A kernel tells you how to change the value of any given pixel by combining it with different amounts of neighbouring pixels.

Used to remove noise, isolation of individual elements, finding intensity bumps or holes in image
"""
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
"""
img=cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)# simple zero would had done
# we need a mask for the transformation which we get from simple thresholding
"""
img=cv2.imread('LinuxLogo.jpg',0)
_, mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
# some black dots are there on balls( white area) because of reflection on balls

kernel=np.ones((4,4),np.uint8)# here the kernel structure is 2x2 square

dilation=cv2.dilate(mask,kernel,iterations=2)# morphological transformation
#maximal pixel value overlapped by kernel and replace image pixel in anchor point position with mthat maximal value
#removes/reduce uncertainities which are less than the kernel size based on neighbouring pixels
# more the iterations more times it will be dilated
# if kernel size is increased then the larger uncertainities will also merge like the shadow in image will merge with the ball if kernel=(5,5)
# due to this dilation brighter portion is increased

erosion=cv2.erode(mask,kernel,iterations=2)#morphological transform
#Like soil erosion it erodes away the boundary of foreground object.The kernel defined slides through the image 
# and a pixel will be considered 1 if all are 1 in the kernel else 0
#here it operates on minimal pixel value
# it makes object in white smaller

opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
# it is erosion followed by dilation

closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
#dilation followed by erosion

mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
# gradient it gets the boundary of objects. difference between dilation and erosion
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)
#top hat . difference between image and opening of image
bh=cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)
#black hat
titles=['Image','mask','Dilation','Erosion','Opening','Closing','Gradient','Top hat','Black hat']
images=[img, mask,dilation,erosion,opening,closing,mg,th,bh]
 
for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()