
import matplotlib
import numpy as np
import cv2
from skimage import morphology, filters
from skimage.util import img_as_ubyte
#import image
import os
import skimage.io
from matplotlib import pyplot as plt
from pathlib import Path
from skimage.morphology import skeletonize


matplotlib.use('TkAgg')


low_yellow = np.array([10, 52, 60])
high_yellow = np.array([60, 255, 255])


def threshold(im):
    # convert into a gray image
    #gray_image = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)

    # convert BGR to HSV
    imgHSV = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    # create the Mask
    mask = cv2.inRange(imgHSV, low_yellow, high_yellow)

    # inverse mask
    # mask = 255-mask
    res = cv2.bitwise_and(im, im, mask=mask)

    binary = mask > filters.threshold_otsu(mask)
    # print(np.unique(binary))

    res = morphology.medial_axis(binary)

    cv_image = img_as_ubyte(res)


    return cv_image



# map1 = image.get_image("map", 'London1.png')
#
# img = image.image_reader(map1)
# #print(img)
#
# im = threshold(img)
# #image.show_image(im)
