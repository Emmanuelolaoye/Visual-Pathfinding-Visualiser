import cv2
import numpy as np
#import image
# import Pixel
#import thresholding

# path = r"images/Saved/Lonn.png"
#img = thresholding.im


# grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def returnIntersections(img):
    # image = cv2.resize(image, ((900), (900)), interpolation=cv2.INTER_CUBIC)

    blur = cv2.GaussianBlur(img, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Find horizontal and verticla lines
    # link to explanation https://stackoverflow.com/questions/7227074/horizontal-line-detection-with-opencv
    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 5))
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 1))

    vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, verticalStructure, iterations=1)  # , iterations=1
    horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontalStructure, iterations=1)

    # performs a bitwise and operation to find where the horizontal and vertical images intersect
    joints = cv2.bitwise_and(horizontal, vertical)
    pixels = np.argwhere(joints == 255)  # this variable is a list that contains all the pixel coordinates of the joints

    # print(returnIntersections(img))

    listOfIntersections = []
    for p in pixels:
        # print(p[0], p[1], "=", im11[p[0], p[1]])# p in pixel is an array od the xy coordinates of the pixel.

        y = p[0]
        x = p[1]

        if img[p[0], p[1]] == 255:
            # print((y, x))
            listOfIntersections.append((y, x))
    #
    #         #cv2.circle(im11, (x, y), 1, (255, 100, 200), 1)
    #     return listOfIntersections
    return listOfIntersections

#listOfInstesections = returnIntersections(img)

# print(grayImage[0][0])
# for px in returnIntersections(img):
#     arr = [255, 255, 0]
#     grayImage[px[0], px[1]] = arr  # turns all the intersection pixels green (for visualisation purposes)
#     # print(image[p[0], p[1]], 2222)

# Pixel.connect_nodes(pixels, image)


# image[100, 100] = (0, 255, 0)
# cv2.imwrite('Testing.png', im11)
# cv2.imshow('thresh',im11)
# cv2.imshow('joints', joints)
# cv2.imshow('horizontal', horizontal)
# cv2.imshow('vertical', vertical)
##cv2.imshow('image', im11)
##
# cv2.waitKey()

# I successfully completed to goal of this issue to find all the intersections of an image I did this by passing in a skeletonised image into the function. then performed 2 morphology operational that created 2 images.
#
# // code placeholder
#
#
#
#
#
# the first image found the horizontal lines and the second vertical. Afterwards 


## idea finding the center of each contour
