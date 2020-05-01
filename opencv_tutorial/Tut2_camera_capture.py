"""
This file has codes to capture images, videos 
from a camera and also display the live content of it
This is reference to Opencv tutorials for beginners part 4
link:https://www.youtube.com/watch?v=-RtVZsCvXAQ&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=5

"""
import cv2
import datetime # for tutorial vid 7 date and time display

cap=cv2.VideoCapture(0)
# cap is now an object of the class VideoCapture
#Arguments: file name like 'sample.avi' or 'sample.mp4' whichever file type it is
#this is to read and operate on a video which is already present. For file in 
# different location give the whole file path in re'...\sample.mp4' this to avoid errors due to \
#or device index which is either 0 or -1 whichever works
# for other cameras connected we can try 1 ,2 ,3 for 2nd , 3rd, 4th and so on

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('Output.avi',fourcc,30.0,(640,480))
# to write output of the captured video with name Output.avi, fourcc code, 30 second length, frame dimensions
# open a while loop to capture the frames continuously


"""
        Tutorial video 6: setting camera parameters
        Uncomment the below mass comment to see results of parameter change
"""
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # prints width of video
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # prints HEIGHT of video
#various other propIDs available at :https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

""" 
cap.set(3,1280) #set(propId,valueChange)
   # Above is equivalent to this cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    #3 is code(index) for frame width property. other codes available at the doc above 
cap.set(4,720)#4 is code for frame height
print(cap.get(3))
print(cap.get(4))
#keep in mind that you can change number to anything but the camera will keep the nearest resolution
#if w,h=700,700 is the change but the resolution will remain 640,480
#or in above case if we pass 1180 instead of 1280 even then it will change it to 1280 only. change will happen till the max value of camera only
"""

while(cap.isOpened()):
    #cap.isopened() returns false if the index is wrong or the file path is wrong
    ret, frame = cap.read() 
    # read is a function of class VidoeCapture to read frames
    # ret will store True or False, True means that the frame is available
    #if frame is available then it will be stored in frame variable
    if ret==True:
        """
            Tutorial video 7:show date and time on live video
            uses knowledge of tut3 file ->puttext
        """
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text=str(datetime.datetime.now())
        #text='Width: '+ str(cap.get(3)) +' Height: '+str(cap.get(4))
        frame = cv2.putText(frame,text,(10,50),font,1,(0,200,200),1,cv2.LINE_AA)
        cv2.imshow('Live',frame)
        out.write(frame)#to write the frames in file till it reaches 30s
        #To live stream the video 
         
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # this function converts frames from one format to
        #to another. BGR represents RGB which is default image setting for color unless
        #changed( as bits are reversed so RGB is written as BGR). for gray scale it is gray
        cv2.imshow('Gray',gray)
        luv=cv2.cvtColor(frame,cv2.COLOR_BGR2Luv)
        cv2.imshow('Luv',luv)#dont know what luv is. given in python when scroll over cvtColor
        bgr=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.imshow('BGR',bgr)
        HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV',HSV) #Hue Saturation Value(brightness)

        #if cv2.waitKey(1)==ord('q') for 32 bit systems as they don't require the mask
        if cv2.waitKey(1) & 0xFF == ord('q'): #mask required for 64 bit systems
            break
        #this will quit when q is pressed

       
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

