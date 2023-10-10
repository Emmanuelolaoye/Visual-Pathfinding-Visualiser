# # import sys
# # import dijalgo
# #
# # from computerVision import image
# # from computerVision import thresholding
# # from computerVision import intersectiondetection
# # #from computerVision import DFSObject
# #
# # import Board
# # import Node
# #
# # list_number = 5
# # empty_grid = []
# # N = sys.maxsize
# #
# #
# # array = [
# #     ["0-0", "0-1", "0-2", "0-3", "0-4"],
# #     ["1-0", "1-1", "1-2", "1-3", "1-4"],
# #     ["2-0", "2-1", "2-2", "2-3", "2-4"],
# #     ["3-0", "3-1", "3-2", "3-3", "3-4"],
# #     ["4-0", "4-1", "4-2", "4-3", "4-4"]
# # ]
# #
# # current_node = array[2][2]
# #
# # for x in range(0, list_number):
# #     for y in range(0, list_number):
# #         print(array[x][y])
# #
# #
# # def getid(node):
# #     x_y = node.split("-")
# #     x = x_y[0]
# #     y = x_y[1]
# #     return
# #     return array[int(node.split("-")[0])][int(node.split("-")[1])]
# #
# #
# # # funtion for up
# # def move_up(node):
# #     # cur node = array[2][2]
# #     return array[int(node.split("-")[0]) - 1][int(node.split("-")[1])]
# #
# #
# # # funtion for down
# # def move_down(node):
# #     return array[int(node.split("-")[0]) + 1][int(node.split("-")[1])]
# #
# #
# # # function for left
# # def move_left(node):
# #     return array[int(node.split("-")[0])][int(node.split("-")[1]) - 1]
# #
# #
# # # function for right
# # def move_right(node):
# #     return array[int(node.split("-")[0])][int(node.split("-")[1]) + 1]
# #
# #
# # # functions for up-left
# # def move_up_left(node):
# #     return array[int(node.split("-")[0]) - 1][int(node.split("-")[1]) - 1]
# #
# #
# # # function for up-right
# # def move_up_right(node):
# #     return array[int(node.split("-")[0]) - 1][int(node.split("-")[1]) + 1]
# #
# #
# # # function for down-left
# # def move_down_left(node):
# #     return array[int(node.split("-")[0]) + 1][int(node.split("-")[1]) - 1]
# #
# #
# # # function for down-right
# # def move_down_right(node):
# #     return array[int(node.split("-")[0]) + 1][int(node.split("-")[1]) + 1]
# #
# #
# #
# # print(f"current node    = {current_node}")
# # print(f"move up         = {move_up(current_node)}")
# # print(f"move down       = {move_down(current_node)}")
# # print(f"move left       = {move_left(current_node)}")
# # print(f"move right      = {move_right(current_node)}")
# # print(f"move up left    = {move_up_left(current_node)}")
# # print(f"move up right   = {move_up_right(current_node)}")
# # print(f"move down left  = {move_down_left(current_node)}")
# # print(f"move down right = {move_down_right(current_node)}")
# # from SourceFile.Board import Board
# #
# # width = 5
# # rows = width
# #
# # board = Board(rows, width)
# #
# # # cur = board.make_grid(width, rows)
# # #
# # # print(cur)
# #
# #
# # matrixx = [
# #
# #     [N, 3, N, N, N, 12, N],
# #     [3, N, 5, N, N, N, 4],
# #     [N, 5, N, 6, N, N, 3],
# #     [N, N, 6, N, 1, N, N],
# #     [N, N, N, 1, N, 10, 7],
# #     [12, N, N, N, 10, N,2],
# #     [N, 4, 3, N, 7, 2, N],
# #
# # ]
# #
# # # toGraph = Board.matrixToGraph(matrixx)
# # #
# # # print(toGraph)
# # #
# # #
# # # printgraph = Board.printgraph(toGraph)
# # # dik = dijalgo.DijkstraAlgorithm(toGraph, "1", "7")
# #
#
# # bImage = thresholding.im
# # intersectionsList = intersectiondetection.returnIntersections(bImage)
# #
# # print(intersectionsList)
#
# import sys
# import dijalgo
# import cv2
# import time
#
# # get the start time
# st = time.time()
#
# #
# # from SourceFile.computerVision import image, DFSObject, thresholding, intersectiondetection, MiscellaneousFunctions
# # from SourceFile.computerVision import thresholding
# # from SourceFile.computerVision import intersectiondetection
# # from SourceFile.computerVision import DFSObject
# # #from SourceFile.computerVision import displayPathOntoImage
# #
# # map1 = image.get_image("map", 'Los Angeles 234-10 3000x2400.png')
# #
# # #London 156-5 3000x2400.png
# # #Los Angeles 234-10 3000x2400.png
# # #Madrid 102-2 3000x2400.png
# # #Paris 120-3 3000x2400.png
# #
# # img = image.image_reader(map1)
# # #print(img)
# # #img = image.resize_image(img, 'relative', 2,2)
# #
# # binaryImage = thresholding.threshold(img)
# #
# #
# #
# # listOfIntersections = intersectiondetection.returnIntersections(binaryImage)
# #
# # graph = DFSObject.recursiveNeighbourhoodGraph(binaryImage, listOfIntersections)
# #
# # DFSObject.printgraph(graph)
# # # #
# #
# # et = time.time()
# #
# # # get the execution time
# # elapsed_time = et - st
# # print('Execution time:', elapsed_time, 'seconds')
# # start = MiscellaneousFunctions.getClosestIntersection((0, 78), listOfIntersections)
# # destination = MiscellaneousFunctions.getClosestIntersection((2376, 1874), listOfIntersections)
# #
# # print(start, destination)
# #
# # path, distance = dijalgo.DijkstraAlgorithm(graph, start, destination)
# #
# # distance = 2/120 * distance
# #
# # print(path, distance)
# # # #
# # img = MiscellaneousFunctions.displayPathOnimage(img, listOfIntersections)
# # #img = image.resize_image(img, 'relative', 2,2)
# # #
# #
# # binaryImage = image.resize_image(binaryImage, 'relative', 2,2)
# # image.show_image(binaryImage)
# #
# # cv2.imwrite("Paris Test file.png",img)
# # img = image.resize_image(img, 'relative', 2,2)
# # image.show_image(img)
#
# import os
#
# def get_filepaths(directory):
#     """
#     This function will generate the file names in a directory
#     tree by walking the tree either top-down or bottom-up. For each
#     directory in the tree rooted at directory top (including top itself),
#     it yields a 3-tuple (dirpath, dirnames, filenames).
#     """
#     file_paths = []  # List which will store all of the full filepaths.
#
#     # Walk the tree.
#     for root, directories, files in os.walk(directory):
#         for filename in files:
#             # Join the two strings in order to form the full filepath.
#             filepath = os.path.join(root, filename)
#             file_paths.append(filepath)  # Add it to the list.
#
#     return file_paths  # Self-explanatory.
#
# # Run the above function and store its results in a variable.
# full_file_paths = get_filepaths(r"M:\22-23_CE301_olaoye_emmanuel_o")
#
#
# for i in full_file_paths:
#     print(i)


from SourceFile.computerVision import image
from tkinter import *
from PIL import ImageTk, Image

mmap = image.get_image("map", 'Madrid 102-2 3000x2400.png')
map = image.image_reader(mmap)
print(mmap)