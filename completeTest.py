import cv2
import os
from PIL import Image
import PIL
import shutil


def runAll(framen, Q):
    # initializations here
    seconds = 10

    fn = (seconds * 10) + 1  # 10fps (frame number)
    speed = 20  # pixel pass per frame
    height = 200  # initial frame height
    width = 200  # initial frame weight
    y = 2000  # starting point
    x = 1000  # starting point

    image = cv2.imread('sunset.jpg')  # use this image to create frames
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    '''
    for i in range(1,fn):
        crop_img = gray[y:y+width, x+((f-1)*speed):height+x+((f-1)*speed)]
        cv2.imwrite("frame {0}.jpg".format(i), crop_img,[int(cv2.IMWRITE_JPEG_QUALITY), Q])
    cv2.waitKey(0)

    '''

    for i in range(1, fn):
        crop_img = gray[y:y + width, x:x + height]
        x = x + speed
        im = Image.fromarray(crop_img)
        im.save('frame {0}.jpg'.format(i), "JPEG", quality=Q, optimize=True)
    cv2.waitKey(10)

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

        imageA = cv2.imread(imageA)
        yy = 0
        xx = speed
        crop_imgx = imageA[yy:yy + nextheight, xx:xx + nextheight]
        return crop_imgx

    nextheight = height
    nextweight = speed
    # this values will be taken from next 'changed' frame region

    for i in range(2, fn):
        img = cv2.imread("frame {0}.jpg".format(i))
        newY = 0
        newX = nextheight - speed

        crop_img = img[newY:newY + nextheight, newX:newX + speed]
        im3 = Image.fromarray(crop_img)
        im3.save('crop {0}.jpg'.format(i), "JPEG", quality=Q, optimize=True)
        cv2.waitKey(10)
        os.remove("frame {0}.jpg".format(i))


    cropRange = 2
    for j in range(1, (fn - 1)):
        list_im = ['frame {0}.jpg'.format(j), 'crop {0}.jpg'.format(cropRange)]
        images2 = [PIL.Image.open(i) for i in list_im]
        append_images(images2)
        combo_1 = append_images(images2)
        combo_1.save('frame {0}.jpg'.format(cropRange), "JPEG", quality=Q, optimize=True)

        # os.remove("crop {0}.jpg".format(j))
        abcd = crop('frame {0}.jpg'.format(cropRange))
        im4 = Image.fromarray(abcd)
        im4.save('frame {0}.jpg'.format(cropRange), "JPEG", quality=Q, optimize=True)

        cropRange = cropRange + 1
    '''
    for z in range (1,fn):
        videoShowE = cv2.imread('frame {0}.jpg'.format(z))
        cv2.namedWindow('Video Show Encoder', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Video Show Encoder', 400, 400)
        cv2.imshow('Video Show Encoder',videoShowE)
        cv2.waitKey(50)
    '''

    #for N in range(2, fn):
       # os.remove('crop {0}.jpg'.format(N))
    for d in range(2, framen):  # use this loop to delete new frames might be used for calculations.
        os.remove('frame {0}.jpg'.format(d))

    for d in range((framen+1), fn):  # use this loop to delete new frames might be used for calculations.
        os.remove('frame {0}.jpg'.format(d))
    for d in range(2, framen):  # use this loop to delete new frames might be used for calculations.
        os.remove('crop {0}.jpg'.format(d))

    for d in range((framen + 1), fn):  # use this loop to delete new frames might be used for calculations.
        os.remove('crop {0}.jpg'.format(d))

    os.rename('crop {0}.jpg'.format(framen), 'cropDec {0}.jpg'.format(Q))

    newpath = 'C:\\Users\\Ilgaz\\PycharmProjects\\untitled\\cropNew {0}'.format(framen)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    shutil.copy('C:\\Users\\Ilgaz\\PycharmProjects\\untitled\\cropDec {0}.jpg'.format(Q),
                'C:\\Users\\Ilgaz\\PycharmProjects\\untitled\\cropNew {0}'.format(framen))


    os.rename('frame {0}.jpg'.format(framen), 'frameDec {0}.jpg'.format(Q))
    newpath ='C:\\Users\\Ilgaz\\PycharmProjects\\untitled\\frameNew {0}'.format(framen)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    shutil.copy('C:\\Users\\Ilgaz\\PycharmProjects\\untitled\\frameDec {0}.jpg'.format(Q),
                'C:\\Users\\Ilgaz\\PycharmProjects\\untitled\\frameNew {0}'.format(framen))

    os.remove('frame 1.jpg')
    os.remove('frameDec {0}.jpg'.format(Q))
    os.remove('cropDec {0}.jpg'.format(Q))
