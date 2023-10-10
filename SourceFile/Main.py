# from tkinter import *
from SourceFile.Gui import Graph
from SourceFile.Gui import gui
import tkinter as tk
from multiprocessing import Process, Manager


def main():
    print("Starting Multiprocessing")

    countries = ["fr", "es", "gb", "us"]  # "eu"

    with Manager() as manager:
        processes = []
        nestedGraphs = manager.list()
        for country in countries:
            # print(country)
            while True:  # makes the program retry in case of Recursion error
                try:
                    p = Process(target=UpdateGraph, args=[country, nestedGraphs])
                    p.start()
                    processes.append(p)
                    break
                except RecursionError:
                    print(f'tried {country} again')
                    continue

        for process in processes:
            process.join()

        nestedGraphs = list(nestedGraphs)
        print("Finished Multiprocessing")

        # for processes in concurrent.futures.as_completed(results):
        #     PRINT(PROCCESES.RESULT())

    print("len of array of graphs: ", len(nestedGraphs))
    win = tk.Tk()
    app = gui.GUI(win, nestedGraphs)
    win.mainloop()
    # UpdateGraph()


def UpdateGraph(country, listOfGraphs):
    # print(9875)
    g, c, i = Graph.Graph(country).getGraph()

    listOfGraphs.append(c)
    listOfGraphs.append(g.copy())
    listOfGraphs.append(i.copy())
    # print(listOfGraphs)


if __name__ == "__main__":
    main()
