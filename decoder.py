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

cropRange=2
for j in range(1,(fn-1)):

    list_im = ['frame {0}.jpg'.format(j), 'crop {0}.jpg'.format(cropRange)]
    images2 = [PIL.Image.open(i) for i in list_im]
    append_images(images2)
    combo_1 = append_images(images2)
    combo_1.save('frame1 {0}.jpg'.format(cropRange))

    #os.remove("crop {0}.jpg".format(j))
    abcd=crop('frame1 {0}.jpg'.format(cropRange))

    cv2.imwrite('frameDec {0}.jpg'.format(cropRange), abcd, [int(cv2.IMWRITE_JPEG_QUALITY), Q])
    Q=Q-1
    cropRange = cropRange +1

for z in range (1,fn):
    videoShowD = cv2.imread('frame {0}.jpg'.format(z))
    cv2.namedWindow('Video Show Decoder', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video Show Decoder', 400, 400)
    cv2.imshow('Video Show Decoder',videoShowD)
    cv2.waitKey(50)

for t in range(2,fn):
    os.remove('frame {0}.jpg'.format(t))

for m in range(2,fn):
    os.remove('frame1 {0}.jpg'.format(m))

os.rename('frame 1.jpg', 'frameDec 1.jpg') #you can use this line for calculations

for d in range(2,fn): #use this loop to delete new frames might be used for calculations.
    os.remove('frameDec {0}.jpg'.format(d))


cv2.waitKey(100)
