"""
Tutorial video 16: Matplotlib with opencv
provides different plots
"""

import cv2 
from matplotlib import pyplot as plt

img=cv2.imread('Lena.jpg',-1)
cv2.imshow('image',img)

plt.imshow(img)
plt.title('Unchnage img file plotted')# opencv reads image in BGR format while matplotlib reads inRGB format
plt.show()

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title('BGR changed to RGB in opencv to plot RGB')
plt.show()
#benefit of matplot lib is that you can save the image, set coordinates, put two or images
#and many more benefits of matplotlib

plt.imshow(img)
plt.title('Without x and y ticks')
plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
# for subplots refer tut8
#for further info go to matplotlib.org
