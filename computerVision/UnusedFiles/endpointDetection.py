import cv2
import numpy as np
# import thresholding
# import image as imgg


# path = 'sample_image.png'
# img = cv2.imread(path, 0)


def endpointDetector(image):
    # Find positions of non-zero pixels
    (rows, columns) = np.nonzero(image)

    # Initialize empty list of coordinates
    endpoint_coordinates = []

    # Loop through all non-zero pixels
    for (row, column) in zip(rows, columns):

        top = max(0, row - 1)
        right = min(image.shape[1] - 1, column + 1)
        bottom = min(image.shape[0] - 1, row + 1)
        left = max(0, column - 1)

        sub_img = image[top: bottom + 1, left: right + 1]
        if np.sum(sub_img) == 255 * 2: # if the pixels only returns 1 neigbour
            endpoint_coordinates.append((row, column))

    return endpoint_coordinates



# img = thresholding.im
#
# endpoint_coords = endpointDetector(img)
#
# print(len(endpoint_coords))
#
# # if endpoint_coords[0] == (0, 251):
# #     print("yes")
#
# print(endpoint_coords)
#