import sys


image = [
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
]


intersections = [(5, 3), (0,2)]
height = len(image)
width = len(image[0])
allPaths = []


def DFS(node, image, path, visitedNodes):
    neighbours = []

    visitedNodes.append(node)
    path.append(node)

    if is_intersection(node) and path[0] != node:
        # store path somewhere
        possiblePaths(path)
        print(path)

    else:

        for directions in range(8):
            nextNode = next_node(node, directions)
            if (inbounds(nextNode) == False) or (is_white(nextNode, image) == False) or (nextNode in visitedNodes):
                #visitedNodes.append(nextNode)
                continue

            DFS(nextNode, image, path, visitedNodes)

    path.pop()
    visitedNodes.remove(node)

    # do bfs search here
    # return node, neighbours # might not need it


def returnAllPaths(node):
    visitedNodes = []

    path = []

    DFS(node, image, path, visitedNodes)


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
    up = (node[0], node[1] - 1)

    return up


def move_down(node):
    down = (node[0], node[1] + 1)

    return down


def move_left(node):
    left = (node[0] - 1, node[1])

    return left


def move_right(node):
    right = (node[0] + 1, node[1])

    return right


def move_up_left(node):
    up_left = (node[0], node[1])

    return up_left


def move_down_left(node):
    down_left = (node[0] - 1, node[1] + 1)

    return down_left


def move_up_right(node):
    up_right = (node[0] + 1, node[1] - 1)

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
    x = node[0]
    y = node[1]

    if x < 0 or x >= width or y < 0 or y >= height:
        return False

    return True


def is_white(node, image):
    try:
        if image[node[0]][node[1]] == 1:
            return True

        return False
    except IndexError:
        return False


def is_intersection(node):
    if node in intersections:
        return True

    return False


def possiblePaths(paths):
    allPaths.append(paths)


# dfs idea
#make a queue and ad the startting point add it to visited
# for each direction rom the starting point

print(returnAllPaths((0, 2)))
