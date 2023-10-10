import math
from pprint import pprint

li = [(1, 2), (2, 2), (3, 5), (8, 3), (3, 5), (8, 7)]
ans = [        1,      2,     5.385,    5.385,   5.385,]



def euclidianDistance(x1, x2, y1, y2):  # to return distance
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))  # √(x2-x1)²+(y2-y1)²

def getCost(list):
    running = True
    while running:
        try:
            tot = 0
            for idx, elem in enumerate(li):

                a = elem
                b = li[(idx + 1)]
                tot += euclidianDistance(a[0],a[1], b[0], b[1])
                print(a,b, " = ", tot)

        except IndexError:
            break
        finally:
            return (tot)


getCost(li)


# add towns and coordinated

# creat key value make that

# print(euclidianDistance(-7, 17, -4, 6))
