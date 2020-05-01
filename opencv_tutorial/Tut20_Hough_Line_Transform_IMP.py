"""
28,29,30
Tutorial 28: Hough Line transform theory
Hough Transform is a popular technique to detect any shape, if you can represent that shape in a mathematical form. It can detect
the shape even if it is broken or distorted a little bit. Can be used to detect lanes on road. First use an edge detector(ex. canny) and then 
represent it in mathematical form(slopes and intecepts).

Hough Transform basics: A line in the image space can be expressed with two variable. For example for cartesian sys yi=mxi+c for polar xcos(theta)+ysin(theta)=r 
For lines in x-y space they can be represented in another way(m[slope]-c[intercept] space). A straight line in xy is represented as a single point in mc space(also known as Hough Space)
When we transform a single point inx-y space then it is a line in mc space with (xo=slope,yo=intercept) of the line in mc space.
So, points in a line in xy space can be represented in mc space with 4 lines interceting at 1 point which will give the slope and intercept of line in xy space.
We can employ same concept in polar coordinates with y= -cos(t)/sin(t)+rx/sin(t). The Hough space(theta-r space)r is y axis. Point in xy space are sinosid curves in theta-r space and intercetion gives x-y line properties
We use polar coordinate system instead of cartesian for hough transform because cartesian method can not represent vertical lines

Hough transform Algorithm:
1.Edge detection( example canny edge detector)
2.Mapping of edge points to the Hough space and storage in an accumulator
3.Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by thresholding and possibly other constraints
4.Conversion of infinite to finite lines.

Two Hough line transforms:1. Standar Hough Transform(HoughLines method)
2.The Probabilistic Hough Line Transform(HoughLinesP method)


Tutorial 29: Hough line Transform using HoughLines method

"""
import cv2
import numpy as np 

img=cv2.imread('sudoku.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# Gray scale images are prefered for Canny edge detection
edges=cv2.Canny(gray,50,150,apertureSize=3)# threshold1=50, threshold2=150, apertureSize=3 for Sobel operator used by canny
lines=cv2.HoughLines(edges,1,np.pi/180,200)
#HoughLines(edge image,rho=distance resolution of accumulator in pixels,theta=angle resolution in radians,threshold) Threshold=>only those lines will be returned which have more votes then threshold
#lines has 2 elements((rho,theta)) because it is in polar coordinates 
# there may be another element votes of the line making it: [[rho,theta],votes]
#Hough transform starts from (0,0) top left corner

for line in lines:
    rho,theta=line[0]
    print(line)
    a=np.cos(theta)
    b=np.sin(theta)
    #converting polar to cartesian
    x0=a*rho
    y0=b*rho
    #x1 stores the rounded off value of rcos(theta)-1000Sin(theta)
    x1=int(x0+1000*(-b))
    #y1 stores rounded off value of rsin(theta)+1000cos(theta)
    y1=int(y0+1000*(a))
    #x2 stores rounded off value of rcos(theta)+1000*sin(theta)
    x2=int(x0-1000*(-b))
    #y2 stores the rounded off value of rsin(theta)-1000*sin(theta)
    y2=int(y0-1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

#some lines are skipped in this method and are infinite long
cv2.imshow('Image Standard method',img)
cv2.imshow('Canny Edge',edges)

"""
Tutorial 30: Hough line transform using HoughLineP
optimised version of HoughLine method
"""

img=cv2.imread('sudoku.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# Gray scale images are prefered for Canny edge detection
edges=cv2.Canny(gray,50,150,apertureSize=3)# threshold1=50, threshold2=150, apertureSize=3 for Sobel operator used by canny
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)# it does not take all the points but rather random optimum points required for line detection
#HoughLinesP(edge image,rho,theta,threshold,minLineLength,maxLineGap)
#minline length : line segments less then this will be rejected
#max line gap is max allowed gap between line segments to treat them as single line

for line in lines:
    x1,y1,x2,y2=line[0]#here we directly get coordinates of line segment
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('image: HoughLineP',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
