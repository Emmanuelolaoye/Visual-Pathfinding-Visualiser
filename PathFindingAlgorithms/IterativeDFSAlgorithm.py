import math

# image = [
#     #        c  c  c  c  c  c  c  c  c  c
#     #        0  1  2  3  4  5  6  7  8  9
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # r0
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # r1
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # r2
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # r3
#     [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],  # r4
#     [1, 1, 1, 0, 0, 1, 0, 1, 1, 1],  # r5
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # r6
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # r7
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # r8
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # r9
#
# listOfIntersections = [(5, 0), (5, 9), (4, 3), (6, 5)]  # (2, 0),

import thresholding
import intersectiondetection

image = thresholding.im
listOfIntersections = intersectiondetection.returnIntersections(image)

rows, columns,  = image.shape

# Create a set of visited nodes
visitedNodes = set()

# Create a dictionary to store subgraphs

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
    up = (node[0] - 1, node[1])

    return up


def move_down(node):
    down = (node[0] + 1, node[1])

    return down


def move_left(node):
    left = (node[0], node[1] - 1)

    return left


def move_right(node):
    right = (node[0], node[1] + 1)

    return right


def move_up_left(node):
    up_left = (node[0] - 1, node[1] - 1)

    return up_left


def move_down_left(node):
    down_left = (node[0] + 1, node[1] - 1)

    return down_left


def move_up_right(node):
    up_right = (node[0] - 1, node[1] + 1)

    return up_right


def move_down_right(node):
    down_right = (node[0] + 1, node[1] + 1)

    return down_right


def is_white(node, image):
    try:
        if image[node[0]][node[1]] == 255 or image[node[0]][node[1]] == 1:
            return True

        return False
    except IndexError:
        return False


def inbounds(node):
    rows = len(image)
    columns = len(image[0])

    # rows, columns, = image.shape

    row = node[0]
    col = node[1]

    if row < 0 or row >= rows or col < 0 or col >= columns:
        return False

    return True


def euclidianDistance(node1, node2):  # to return distance
    x1 = node1[0]
    y1 = node1[1]
    x2 = node2[0]
    y2 = node2[1]

    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def generate_graph(image, listOfIntersections):
    visitedNodes = set()
    graph = {}


    for intersection in listOfIntersections:
        stack = [(intersection, [intersection])]  # Stack with current node and path

        while stack:
            current_node, path = stack.pop()

            visitedNodes.add(current_node)

            if current_node != intersection and current_node in listOfIntersections:
                subgraph = {}
                for node in path:
                    if node != intersection:
                        subgraph[node] = euclidianDistance(node, current_node)
                graph[current_node] = subgraph

            for direction in range(8):
                next_node_coord = next_node(current_node, direction)

                if (
                    inbounds(next_node_coord)
                    and is_white(next_node_coord, image)
                    and next_node_coord not in visitedNodes
                ):
                    stack.append((next_node_coord, path + [next_node_coord]))

    return graph


graph = generate_graph(image, listOfIntersections)

# Print the graph
for key in graph:
    print(key, "-->", graph[key])
