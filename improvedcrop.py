import cv2
import numpy

#initializations here
Q=100
seconds=10
fn=(seconds*10)+1 #10fps (frame number)
speed=20 #pixel pass per frame
height = 200 #initial frame height
width = 200 #initial frame weight
y = 2076 #starting point
x = 1464 #starting point

image=cv2.imread('sunset.jpg') #use this image to create frames
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(1,fn):
    crop_img = gray[y:y+width, x:x+height]
    x=x+speed
    cv2.imwrite("frame {0}.jpg".format(i), crop_img,[int(cv2.IMWRITE_JPEG_QUALITY), Q])
cv2.waitKey(0)

