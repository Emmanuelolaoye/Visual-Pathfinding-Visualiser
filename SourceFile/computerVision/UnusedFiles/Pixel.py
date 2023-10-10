from collections import deque
import sys

import thresholding
import numpy as np
import intersectiondetection as id

# the goal of this file is to take a take in a list of intersection pixels and find all the connected pixels and
# return in to a neighbourhood representation to run dijkstras algorithm


# to start with every pixel has an (x,y) coordinate location and a colour which i black or white as it has been turned
# into a binary image.

# since the roads have been skeleton to 1 pixel wide, there should only be the start pixel, the previous pixel
# and the next pixel. the only pixels tht will have more that are intersection pixels.
# queue = popleft fifo
# stack # pop lifo

# proposed steps to complete project.
img = thresholding.im
height, width = img.shape
intersections = id.white_pixels
intersectionsQueue = deque(intersections)

# print(img)
# print(len(np.unique(img, axis=0, return_counts = True)))  # number of unique colours in the image should be 2 if not its not a binary image


# print(x, y, "=", img[x, y])

# make a list for visited pixels. this will stop needing to check pixels again

blackpx = 0
whitepx = 255


def connect_nodes(intersections, image):
    intersectionsQueue = intersections
    visted_px = []
    handled_px = []  # could be a queue
    # current_node = () # might be unneeded

    while len(intersectionsQueue) > 0:
        current_node = intersectionsQueue.popleft()

        x = current_node[0]
        y = current_node[1]


        #Dfs_search(node, img) #todo add DFS Search Algo here (i believe)
            # node should find its neighbours

        print(current_node, '=', image[x, y])


# todo pop out intersesection so it doent say its self use itsself as a goal node

def DFS(node, image):

    neighbours = []

    for directions in range(8):
        pass

    # do bfs search here
    return node, neighbours





def next_node(node, index):  # todo add parameter that will designate the direction to go to with number
    up = move_up(node)
    down = move_down(node)
    left = move_left(node)
    right = move_right(node)
    up_left = move_up_left(node)
    up_right = move_up_right(node)
    down_left = move_down_left(node)
    down_right = move_down_right(node)

    directions = [up, down, left, right, up_left, up_right, down_left, down_right]

    return directions[index]


def move_up(node):
    up = node[0], node[1] - 1

    return up


def move_down(node):
    down = node[0], node[1] + 1

    return down


def move_left(node):
    left = node[0] - 1, node[1]

    return left


def move_right(node):
    right = node[0] + 1, node[1]

    return right


def move_up_left(node):
    up_left = node[0], node[1]

    return up_left


def move_down_left(node):
    down_left = node[0] - 1, node[1] + 1

    return down_left


def move_up_right(node):
    up_right = node[0] + 1, node[1] - 1

    return up_right


def move_down_right(node):
    down_right = node[0] + 1, node[1] + 1

    return down_right


def find_colour(node, image):
    try:
        return image[node[0], node[1]]

    except IndexError:
        sys.exit()


def inbounds(node):
    x = node[0]
    y = node[1]

    if x < 0 or x > width or y < 0 or y > height:
        return False

    return True


def is_white(node, image):
    if image[node[0], node[1]] == 255:
        return False

    return True


def is_intersection(node):
    if node in intersections:
        return True

    return False


connect_nodes(intersections, img)

'''
to make a successful algorithim BFS needs to be implemented

'''
