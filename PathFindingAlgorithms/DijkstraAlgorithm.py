import sys
from heapq import heappush, heappop


def DijkstraAlgorithm(graph, start, goal):
    infinity = sys.maxsize
    shortest_distance = {}
    track_predecessor = {}
    track_path = []
    unseen_nodes = {}
    tempgraph = graph
    unseen_nodes.update(tempgraph)  # because the algorithm keeps deleting the graph

    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        (min_distance, min_distance_node) = heappop(priority_queue)

        if min_distance > shortest_distance[min_distance_node]:
            continue

        path_options = graph[min_distance_node].items()
        for neighbouring_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[neighbouring_node]:
                shortest_distance[neighbouring_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[neighbouring_node] = min_distance_node
                heappush(priority_queue, (shortest_distance[neighbouring_node], neighbouring_node))

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            return False, False

    track_path.insert(0, start)

    if shortest_distance[goal] != infinity:
        return track_path, shortest_distance[goal]


# graph = {
#     'A': {'B': 3, 'C': 4, 'D': 7.5},
#     'B': {'C': 1, 'F': 5},
#     'C': {'F': 6, 'D': 2},
#     'D': {'E': 3, 'G': 6},
#     'E': {'G': 3, 'H': 4},
#     'F': {'E': 1, 'H': 8},
#     'G': {'H': 2},
#     'H': {'G': 2}
#
# }

adjacencyList = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 4, 'E': 3},
    'C': {'D': 4, 'E': 5},
    'D': {},
    'E': {'D': 1},

}

# print(graph["A"].items())
# print(dij_recursive(graph, 'A', 'C'))
# print(DijkstraAlgorithm(graph, 'A', 'C'))
# print(DijkstraAlgorithm(graph, 'A', 'C'))


'''
Alternative solutions to Dijkstra's algorithm



# def DijkstraAlgorithm(graph, start, goal):
#     infinity = sys.maxsize
#     shortest_distance = {}
#     track_predecessor = {}
#     track_path = []
#     unseen_nodes = {}
#     tempgraph = graph
#     unseen_nodes.update(tempgraph)  # because the algorithm keeps deleting the graph
#
#     for node in unseen_nodes:
#         shortest_distance[node] = infinity
#     shortest_distance[start] = 0
#
#     while unseen_nodes:
#         min_distance_node = None
#         for node in unseen_nodes:
#
#             if min_distance_node is None:
#                 min_distance_node = node
#             elif shortest_distance[node] < shortest_distance[min_distance_node]:
#                 min_distance_node = node
#
#         path_options = graph[min_distance_node].items()
#         for child_node, weight in path_options:
#
#             if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
#                 shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
#                 track_predecessor[child_node] = min_distance_node
#
#         unseen_nodes.pop(min_distance_node)
#     currentNode = goal
#
#     while currentNode != start:
#         try:
#             track_path.insert(0, currentNode)
#             currentNode = track_predecessor[currentNode]
#         except KeyError:
#             return False, False
#
#     track_path.insert(0, start)
#
#     if shortest_distance[goal] != infinity:
#         return track_path, shortest_distance[goal]


# def DijkstraAlgorithm_recursive(graph, start, goal):
#     infinity = sys.maxsize
#     shortest_distance = {}
#     track_predecessor = {}
#     track_path = []
#     unseen_nodes = {}
#     tempgraph = graph
#     unseen_nodes.update(tempgraph)
# 
#     for node in unseen_nodes:
#         shortest_distance[node] = infinity
#     shortest_distance[start] = 0
# 
#     def recursive_helper(current_node):
#         if not unseen_nodes:
#             return
# 
#         min_distance_node = None
#         for node in unseen_nodes:
#             if min_distance_node is None or shortest_distance[node] < shortest_distance[min_distance_node]:
#                 min_distance_node = node
# 
#         if min_distance_node == goal:
#             build_path(goal)
#             return
# 
#         path_options = graph[min_distance_node].items()
#         for child_node, weight in path_options:
#             if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
#                 shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
#                 track_predecessor[child_node] = min_distance_node
# 
#         unseen_nodes.pop(min_distance_node)
# 
#         recursive_helper(min_distance_node)
# 
#     def build_path(node):
#         if node != start:
#             build_path(track_predecessor[node])
#         track_path.append(node)
# 
#     recursive_helper(start)
# 
#     if shortest_distance[goal] != infinity:
#         return track_path, shortest_distance[goal]
'''
