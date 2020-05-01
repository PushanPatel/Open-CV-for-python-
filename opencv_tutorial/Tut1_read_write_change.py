import cv2
"""
3,10(add)
Refer: https://docs.opencv.org/4.0.0 for various definitions present in opencv(cv2) module
Tutorial video 3 
cv2.imread('image.jpg',flag)
From github repository OpenCv in D: drive go to tutorial/opencv.html to see important things such as flag
    flags are arguments given while reading image in order to represent the read file in color,gray or no change respectively
1,0,-1 respectively for color,gray,no change
"""
img = cv2.imread('lena.jpg', 0)
"""
second method: l= r"D:\Vs_code_opencv_workspace\opencv_tutorial\lena.jpg"   that is the path of the image
    img.cv2.imread(l,0)
"""
print(img)# if it prints none then file name or file path is wrong. else it will give a matrix

cv2.imshow('image',img)#To display a window with title image which contains the photo stored in img
cv2.waitKey(5000)# To wait till 5s and then disappear, use 0 as argument in order to make it disappear when a key is pressed
cv2.destroyAllWindows()# to destroy all the created windows

cv2.imwrite('lena_bw.jpg',img)# to create an output of the image in the folder with file name 

# you can use k= cv2.waitKey(0) or k=cv2.waitKey(0)&0xFF 
# if k == ord('s'):   ord('s') gives value for s key when pressed om keybard that is stored in k

"""
Tutorial vidoe 10:cv.split,cv.merge,cv.resize,cv.add
"""
img = cv2.imread('messi5.jpg', 1)
print(img.shape)#Returns tuple of number of rows, columns and channels
print(img.size)# Returns total number of pixels accessed # reduces by 3 when converted to gray(bw) image
print(img.dtype)# Returns image datatype same for both bw and color image
he, wi,channels = img.shape# for a black and white image there will be no parameter as channels
print (he, wi)

b,g,r=cv2.split(img)# splits the image into B,G,R channels resp.
img=cv2.merge((b,g,r))# merges B,G,R channels passed to it into an image

"""
ROI= Region of interest: it is the part/region of image that we want to work on 
following is an example of selecting a region and then pasting it on another region.
This is an example from the video with preknowledge of coordinates on pic by the instructor

"""
ball=img[280:340,330:390]# storing the ROI. These are coordinates known by instructor
img[273:333, 100:160]=ball # pasting the ROI on another region
cv2.imshow('Image',img)

img2=cv2.imread('Lena.jpg',1)
img=cv2.resize(img,(512, 512)) #this function resizes the image to the mentioned parameters. Here only dimension is passed. dimension=(width,height)
img2=cv2.resize(img2,(512,512))
Add=cv2.add(img,img2) # add(var1,var2) adds two images (provided the array sizes are same for both). 
AW=cv2.addWeighted(img,0.8,img2,0.2,0)# adds image sources with different weightage plus any scalar
#This can be used to give your watermarks
cv2.imshow('ADD',Add)
cv2.imshow('AddWeighted',AW)


# function from stackflow to resize oversized images to desired width or height or both
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    elif height is None:
        r = width / float(w)
        dim = (width, int(h*r))
    else:      #function changed a bit to accomodate this too
        print(width,height)
        dim = (width, height)

    return cv2.resize(image, dim, interpolation=inter)

im=cv2.imread('me1.jpg',0)
new_im=ResizeWithAspectRatio(im,height=800)
new_im2=ResizeWithAspectRatio(im,width=800)
cv2.imshow('New1',new_im)
cv2.waitKey(5000)
cv2.imshow('New2',new_im2)
cv2.imwrite('me1compressed.jpg',new_im)
cv2.waitKey(5000)

im=cv2.imread('nature1.jpg',1)
new_color=ResizeWithAspectRatio(im,height=800)
cv2.imshow('New2',new_color)
cv2.imwrite('colorcompressed.jpg',new_color)
cv2.waitKey(5000)
cv2.destroyAllWindows()

