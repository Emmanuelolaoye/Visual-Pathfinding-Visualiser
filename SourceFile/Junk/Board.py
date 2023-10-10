import sys

inf = sys.maxsize

matrix = [

    [1, inf, inf, inf, 9],
    [inf, 2, inf, inf, inf],
    [3, inf, 3, inf, inf],
    [inf, 7, inf, 4, inf],
    [inf, inf, inf, inf, 5]

]


class Board:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def Move_up(self):
        if self.node.x > 0:
            self.node.x = self.node.x - 1
        return self.node

    def Move_down(self, node):
        if (node.x + 1 < self.height):
            node.x = node.x + 1
        return node

    def Move_left(self, node):
        if (node.y > 0):
            node.y = node.y - 1
        return node

    def Move_right(self, node):
        if (node.y + 1 < self.height):
            node.y = node.y + 1
        return node

    def make_grid(self, height, width):  # to create a grid of said height and width
        row = height
        array = []
        # gap = width // rows
        for row in range(row):
            rows = []
            for col in range(width):
                rows.append(f"{row} - {col}")

            array.append(rows)

        return array

    # N = sys.maxsize
    # matrixx = [
    #
    #     [N, 3, N, N, N, 12, N],
    #     [3, N, 5, N, N, N, 4],
    #     [N, 5, N, 6, N, N, 3],
    #     [N, N, 6, N, 1, N, N],
    #     [N, N, N, 1, N, 10, 7],
    #     [12, N, N, N, 10, N, 2],
    #     [N, 4, 3, N, 7, 2, N],
    # sotre main roads
    # ]

    def matrixToGraph(m):
        # to turn an adjacency matrix to a graph so dijkstra can be performed on it

        graph = {}
        for rows in m:
            subgraph = {}
            for col in rows:
                if col == inf:
                    continue
                subkey = str((rows.index(col)) + 1)
                subgraph[subkey] = col

            key = str((m.index(rows)) + 1)
            graph[key] = subgraph

        return graph

    eg_array = [
        ["0-0", "0-1", "0-2", "0-3", "0-4"],
        ["1-0", "1-1", "1-2", "1-3", "1-4"],
        ["2-0", "2-1", "2-2", "2-3", "2-4"],
        ["3-0", "3-1", "3-2", "3-3", "3-4"],
        ["4-0", "4-1", "4-2", "4-3", "4-4"]
    ]

    graph = {
        'A': {'B': 3, 'C': 4, 'D': 7},
        'B': {'C': 1, 'F': 5},
        'C': {'F': 6, 'D': 2},
        'D': {'E': 3, 'G': 6},
        'E': {'G': 3, 'H': 4},
        'F': {'B': 1, 'C': 8},
        'G': {'E': 1, 'F': 8},
        'H': {'A': 1, 'D': 8},

    }

    # cur_node = array[2][2]

    # print(Board.Move_up(cur_node))

    def printgraph(graph):

        for key in graph:
            print(key, "-->", graph[key])
            # for subkey in graph[key]:
            #     print(subkey,"->", graph[key][subkey] )


#
# Pgraph = {}
# for rows in matrix:
#     subgraph = {}
#     for col in rows:
#         if col == inf:
#             continue
#         subkey = str(rows.index(col))
#         subgraph[subkey] = col
#
#     key = str(matrix.index(rows))
#     Pgraph[key] = subgraph


# print(Pgraph, 12211)
#
# for key in Pgraph:
#     print(key ,"-->",Pgraph[key])
#     for subkey in Pgraph[key]:
#         print(subkey,"->", Pgraph[key][subkey])


# Mgraph = {}
#
# subgraph = {}
# subgraph1 = {}
#
#
# subgraph["A"] = 3
# subgraph["B"] = 4
# Mgraph["A"] = subgraph
# Mgraph["E"] = subgraph
#
# #neighbourhood represewntation
#
# print(Mgraph)

# print(matrixToGraph(matrixx))


xs = [(1, 1), (2, 2), (3, 3)]

s = ''.join(str(x) for x in xs)

print(s)
