import math
import sys

#rows, columns,  = image.shape

#print(len(image), len(image[0]))
#print(intersections)

image = [
    #        c  c  c  c  c  c  c  c  c  c
    #        0  1  2  3  4  5  6  7  8  9
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # r0
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # r1
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # r2
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # r3
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],  # r4
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 1],  # r5
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # r6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # r7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # r8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # r9


listOfIntersections = [(5, 0), (5, 9), (4, 3), (6, 5)]  # (2, 0),
#startingNode = (listOfIntersections[999])



subgraph = {}
def DFS(node, image, path, visitedNodes):
    # print(badnodes)
    neighbours = []

    visitedNodes.append(node)
    path.append(node)

    # if node in end_node:
    #     tempPath = path.copy()
    #     endpointsPath.extend(tempPath)
    # print(path)

    # if node == (2, 5):
    #     print(232323546)

    if is_intersection(node) and path[0] != node:
        # store path somewhere
        # print("yes")
        tempPath = path.copy()
        possiblePaths(tempPath)

        # print(path)
        # print("make sure")

    else:

        for directions in range(8):
            nextNode = next_node(node, directions)

            # if nextNode == (2,5):
            #     print(nextNode, inbounds(nextNode), " - inbounds", is_white(node, image), "- iswhite", nextNode in badnodes, "- inbadnodes")

            if (inbounds(nextNode) == False) or (is_white(nextNode, image) == False) or (nextNode in visitedNodes):
                # badnodes.add(node)
                # visitedNodes.append(nextNode)
                # print(visitedNodes)
                continue
            # print(nextNode)
            DFS(nextNode, image, path, visitedNodes)

    # print("did you get here?")
    path.pop()
    visitedNodes.remove(node)
    # path.clear()
    # path.append(startingNode)

    # do bfs search here
    # return node, neighbours # might not need it


def returnAllPaths(node):
    visitedNodes = []
    path = []
    return DFS(node, image, path, visitedNodes)
    # print("anything here?")
    # print(allPaths)


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


def find_colour(node, image):
    try:
        return image[node[0], node[1]]

    except IndexError:
        sys.exit()


def inbounds(node):
    rows = len(image)
    columns = len(image[0])

    #rows, columns, = image.shape

    row = node[0]
    col = node[1]

    if row < 0 or row >= rows or col < 0 or col >= columns:
        return False

    return True


def is_white(node, image):
    try:
        if image[node[0]][node[1]] == 255 or image[node[0]][node[1]] == 1:
            return True

        return False
    except IndexError:
        return False


def is_intersection(node):
    if node in listOfIntersections:
        return True

    return False


def removeEndpoints():
    pass  # todo create function that removes endpoints paths (******might not need)


def possiblePaths(paths):
    allPaths.append(paths)


def pathLength(path):
    # todo create function that counts the path length  left, right, up, down is +1 / diagonal = +Sqrt(1)
    startNode = path[0]
    endNode = path[-1]
    radicalOf2 = math.sqrt(2)
    one = 1
    PathLength = 0

    for index in range(len(path) - 1):

        if euclidianDistance(path[index], path[index + 1]) == 1:
            PathLength += 1

        elif euclidianDistance(path[index], path[index + 1]) == radicalOf2:
            PathLength += radicalOf2

        else:
            return False
        pass

    return [startNode, endNode, PathLength]


def isAdjacent(current_node, next_node):
    if move_left(current_node) == next_node:
        return True, "S"

    return False


def euclidianDistance(node1, node2):  # to return distance
    x1 = node1[0]
    y1 = node1[1]
    x2 = node2[0]
    y2 = node2[1]

    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))



def subgraphMaker(path):
    subkey = path[1]
    subgraph[subkey] = path[2]

    return subgraph


def subgraphAdder(graph, subgraph, node):

    graph[node] = subgraph


def printgraph(graph):

    for key in graph:
        print(key, "-->", graph[key])
# ****dfs idea****
# make a queue and ad the starting point add it to visited
# for each direction rom the starting point


graph = {}

for intersections in listOfIntersections:
    allPaths = []
    returnAllPaths(intersections)
    #print(allPaths)

    subgraph = {}
    for paths in allPaths:
        #print(paths, pathLength(paths))
        subgraphMaker(pathLength(paths))
        subgraphAdder(graph, subgraph, intersections)



printgraph(graph)

