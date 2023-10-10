from SourceFile.computerVision import image, thresholding, intersectiondetection, MiscellaneousFunctions
from PathFindingAlgorithms import RecursiveDfsAlgorithm, DijkstraAlgorithm
import warnings


franceGraph = {}
usaGraph = {}
gbGraph = {}
spainGraph = {}


class Graph:
    def __init__(self, country):
        self.country = country
        pass

    def getBinaryImage(self):
        if self.country == "es":
            mmap = image.get_image("map", 'Madrid 102-2 3000x2400.png')

        elif self.country == "fr":
            mmap = image.get_image("map", 'Paris 120-3 3000x2400.png')

        elif self.country == "us":
            mmap = image.get_image("map", 'Los Angeles 234-10 3000x2400.png')

        elif self.country == "gb":
            mmap = image.get_image("map", 'London 156-5 3000x2400.png')

        else:
            warnings.warn('Bad Country Argument!')

        img = image.image_reader(mmap)

        return thresholding.threshold(img)

    def getIntersections(self):
        #print(f"getting {self.country} Intersections")
        return intersectiondetection.returnIntersections(self.getBinaryImage())

    def getGraph(self):
        uppercase = str(self.country).upper()
        intersection = self.getIntersections()

        print(f"Getting {uppercase} Graph")
        graph = RecursiveDfsAlgorithm.recursiveNeighbourhoodGraph(self.getBinaryImage(), intersection)
        #graph = DFSObject.iterativeNeighbourhoodGraph(self.getBinaryImage(), intersection)
        print(f"Got {uppercase} Graph")

        return graph, uppercase, intersection

        pass

    def getShortestPath(self, start, destination, graph):
        start = MiscellaneousFunctions.getClosestIntersection(start, self.getIntersections())
        destination = MiscellaneousFunctions.getClosestIntersection(destination, self.getIntersections())
        # print(start, destination)

        return DijkstraAlgorithm.DijkstraAlgorithm(graph, start, destination)


# def getGraph(country):
#     print(9875)
#     if country == "es":
#         Graph(spainGraph, country).getGraph()
#     elif country == "fr":
#         Graph(franceGraph, country).getGraph()
#     elif country == "us":
#         Graph(usaGraph, country).getGraph()
#     elif country == "gb":
#         Graph(gbGraph, country).getGraph()


# countries = ["es", "fr", "gb", "us"]
# with concurrent.futures.ProcessPoolExecutor() as executor:
#
#     f1 = executor.submit(dosomething, 1)
#     print(f1.result())

# for procceses in concurrent.futures.as_completed(results):
#     print(procceses.result())


# if __name__ == '__main__':
#     s = perf_counter()
#
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#
#         countries = ["es", "fr", "gb", "us"]
#         results = [executor.submit(getGraph, country) for country in countries]
#
#     # for procceses in concurrent.futures.as_completed(results):
#     #     print(procceses.result())
#
#     f = perf_counter()
#
#     print(f'\nFinished in {round(f - s, 5)} second(s)')

# graph = {}
#
# graphmaker = Graph(graph, 'fr').getGraph()


# print(graphmaker)
