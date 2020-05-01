import numpy as np
import cv2
#img=cv2.imread('me1compressed.jpg',1)
img=np.zeros([800,600,3],np.uint8)
#makes a black image using numpy, np.zeros([height,width,3],np.datatype) uint8= byte which is used here

img=cv2.line(img,(0,0),(300,300),(255,0,155),5) 
#can use another variable to store the values so as not to change img. Here it is getting updated
#draws a line ->line(imgvariable,start_point,end_point,color,thickness)
#start_point and end point are with respect to top left corner(0,0) and thickness in pixels
#color is in RGB format so the input will be (B,G,R) where B,G,R are the respective concentration values ranging from 0 to 255
 # if the image is read in gray scale flag then line colors will be black except when (255,255,255)

img=cv2.arrowedLine(img,(300,400),(600,400),(155,155,0),2)
#same as line just an arrow will be there at end point

img=cv2.rectangle(img,(500,500),(550,600),(0,200,100),6)#if you increas thickness then it increases from middle
#rectangle(variable,topleftcorner,bottomrightpoint,color,thickness,linetype,shift)
#if thickness=-1 then it will fill the rectangle
img=cv2.rectangle(img,(500,500),(550,600),(0,100,200),-5)

img=cv2.circle(img,(525,550),20,(155,155,155),3)
#circle(var,center,radius,color,thickness,shift)
font=cv2.FONT_HERSHEY_TRIPLEX
img=cv2.putText(img,'OpenCv',(10,500),font,2,(100,150,200),4,cv2.LINE_AA)
#inserts text-> puttext(var,'Text',startPoint,font,fontsize,color,thick,linestyle)
# does not take \n character

#other shapes are elipse, polygon
cv2.imshow('Result',img)

cv2.waitKey(2000)
cv2.destroyAllWindows()