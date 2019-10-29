import cv2
import numpy as np
import os
from PIL import Image
import PIL
from improvedcrop import speed,fn,height,Q


def append_images(images, bg_color=(255, 255, 255)):
    widths, heights = zip(*(i.size for i in images))
    new_width = sum(widths)
    new_height = max(heights)
    new_im = Image.new('RGB', (new_width, new_height), color=bg_color)
    offset = 0
    for im in images:
        y = new_height - im.size[1]
        new_im.paste(im, (offset, y))
        offset += im.size[0]

    return new_im

def crop(imageA):


    imageA= cv2.imread(imageA)
    yy=0
    xx=speed
    crop_imgx = imageA[yy:yy+nextheight, xx:xx+nextheight ]
    return crop_imgx


nextheight=height
nextweight=speed
#this values will be taken from next 'changed' frame region

for i in range(2,fn):

    img= cv2.imread("frame {0}.jpg".format(i))
    newY=0
    newX=nextheight-speed

    crop_img = img[newY:newY+nextheight, newX:newX+speed]
    cv2.imwrite('crop {0}.jpg'.format(i), crop_img, [int(cv2.IMWRITE_JPEG_QUALITY), Q])
    os.remove("frame {0}.jpg".format(i))
    Q=Q-1

Q=100
list_im = ['frame 1.jpg', 'crop 2.jpg']
images1 = [PIL.Image.open(i) for i in list_im]
append_images(images1)
combo_2 = append_images(images1)
combo_2.save('frame 2.jpg')
img = cv2.imread('frame 2.jpg')
lastY = 0
lastX = speed
crop_img2 = img[lastY:lastY + nextheight, lastX:lastX + (nextheight+speed)]
cv2.imwrite('frame 2.jpg', crop_img2, [int(cv2.IMWRITE_JPEG_QUALITY), (Q-1)])



cropRange=3
for j in range(2,(fn-1)):

    list_im = ['frame {0}.jpg'.format(j), 'crop {0}.jpg'.format(cropRange)]
    images2 = [PIL.Image.open(i) for i in list_im]
    append_images(images2)
    combo_1 = append_images(images2)
    combo_1.save('frame {0}.jpg'.format(cropRange))

    #os.remove("crop {0}.jpg".format(j))
    abcd=crop('frame {0}.jpg'.format(cropRange))

    cv2.imwrite('frame {0}.jpg'.format(cropRange), abcd, [int(cv2.IMWRITE_JPEG_QUALITY), Q])
    Q=Q-1

    cropRange = cropRange +1

for z in range (1,fn):
    videoShowE = cv2.imread('frame {0}.jpg'.format(z))
    cv2.namedWindow('Video Show Encoder', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video Show Encoder', 400, 400)
    cv2.imshow('Video Show Encoder',videoShowE)
    cv2.waitKey(50)

 #   cv2.imshow('ccc', abcd)
#for t in range(2,fn):
#   os.remove('frame {0}.jpg'.format(t))



cv2.waitKey(100)