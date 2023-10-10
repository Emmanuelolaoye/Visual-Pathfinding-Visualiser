from tkinter import Canvas, PhotoImage, messagebox
from tkinter.constants import NW
from PathFindingAlgorithms import DijkstraAlgorithm
from SourceFile.computerVision import MiscellaneousFunctions


# import os
# os.system('cls')

class MapWindow():

    def __init__(self, frame, country, graphOfCountry, intersectionsOfCountry):
        self.frame = frame
        self.country = country
        self.counter = []
        self.mapCanvas = Canvas(self.frame, width=1010, height=810)
        self.graphOfCountry = graphOfCountry
        self.intersections = intersectionsOfCountry



        #self.intersections = Graph.Graph(self.country).getIntersections()
        # print(self.country)
        self.loadCountryFrame()

        #DFSObject.printgraph(graphOfCountry)

        # for i in self.graphOfCountry:
        #     print(i)

        #print(self.graphOfCountry)
        print("\n\n")
        #print(self.intersections)

    def clickcounter(self, tag):
        self.counter.append(tag)

        if len(self.counter) == 2:
            print(self.counter)
            self.mapCanvas.delete("!clicked")
            self.getShortestPath(self.counter[0], self.counter[1])

            # hello()
            self.counter.clear()

    def stringToTuple(self, tup):

        tup = tup.replace("(", "").replace(")", "")
        # print(tup)
        tup = tup.split(",")
        tup = (int(tup[0]), int(tup[1]))
        return tup

    def getNearestPoint(self, point):
        MiscellaneousFunctions.getClosestIntersection()
        pass

    def getShortestPath(self, start, destination):
        try:
            start = self.stringToTuple(start)
            destination = self.stringToTuple(destination)

            start = MiscellaneousFunctions.getClosestIntersection(start, self.intersections)
            destination = MiscellaneousFunctions.getClosestIntersection(destination, self.intersections)
            # print(start, destination)

            # print(start, destination)

            path, distance = DijkstraAlgorithm.DijkstraAlgorithm(self.graphOfCountry, start, destination)

            convertedDistnce = self.pixelTOKilometer(distance)

            self.loadShortestPath(path)
            messagebox.showinfo("Shortest Path", f"Distance {start} to {destination}, is {convertedDistnce}Km.")
            return path

        except Exception:
            messagebox.showinfo("Path not found", f"Unable to find path from {start} to {destination}\n,Please select clear all and try again!!")
        #
        # path = dijalgo.DijkstraAlgorithm(self.graphOfCountry, start, destination)
        # print(path)
        # pass

    def destroyCanvas(self):
        self.frame.destroy()
        pass

    def pixelTOKilometer(self, distance):
        if self.country == "gb":
            distance = 5 / 156 * distance
        elif self.country == "us":
            distance = 10 / 234 * distance
        elif self.country == "fr":
            distance = 2 / 120 * distance
        elif self.country == "es":
            distance = 2 / 201 * distance

        return round(distance, 2)

    def loadCountryFrame(self):
        global backgoundImage
        # self.destroyCanvas()

        if self.country == "gb":
            backgoundImage = self.getBackgroundImage()
            # mapCanvas = Canvas(self.frame, width=1010, height=810)
            self.mapCanvas.pack()
            self.mapCanvas.create_image(0, 0, anchor=NW, image=backgoundImage, tag='clicked')
            pass

        elif self.country == "us":
            backgoundImage = self.getBackgroundImage()
            # mapCanvas = Canvas(self.frame, width=1010, height=810)
            self.mapCanvas.pack()
            self.mapCanvas.create_image(0, 0, anchor=NW, image=backgoundImage, tag='clicked')
            pass

        elif self.country == "fr":
            backgoundImage = self.getBackgroundImage()

            self.mapCanvas.pack()
            self.mapCanvas.create_image(0, 0, anchor=NW, image=backgoundImage, tag='clicked')

            pass

        elif self.country == "es":
            backgoundImage = self.getBackgroundImage()
            # mapCanvas = Canvas(self.frame, width=1010, height=810)
            self.mapCanvas.pack()
            self.mapCanvas.create_image(0, 0, anchor=NW, image=backgoundImage, tag='clicked')
            pass

        else:
            return False

    def getBackgroundImage(self):
        if self.country == "gb":
            return PhotoImage(file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\London 52-5 1000x800.png")

        elif self.country == "us":
            return PhotoImage(
                file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Los Angeles 78x10 1000x800.png")

        elif self.country == "fr":
            return PhotoImage(file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Paris 40-2 1000x800.png")

        elif self.country == "es":
            return PhotoImage(file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Madrid 34-2 1000x800.png")

        else:
            return False

    # f = Frame(win, width=300, height=300, bg = 'blue')
    #
    # f.place(anchor='center', relx=0.5, rely=0.5)

    def createPoint(self, x, y, r, tag, info):  # center coordinates, radius
        # print(x, y, r, tag, info)


        def showMessage():
            self.mapCanvas.itemconfig(t, text=tag + " " + info)
            self.mapCanvas.itemconfig(rr, fill="blue")
            # Get the bounding box of text
            bbox = self.mapCanvas.bbox(t)

            # Outline the canvas text
            rect = self.mapCanvas.create_rectangle(bbox, outline="black", fill="white", tags="rect")
            self.mapCanvas.tag_raise(t, rect)

        def hideMessage():
            self.mapCanvas.itemconfig(t, text="")
            self.mapCanvas.itemconfig(rr, fill="green")
            self.mapCanvas.delete("rect")

        def dontHideMessage(tag):
            self.mapCanvas.delete("rect")
            self.mapCanvas.tag_unbind(rr, '<Leave>')
            self.mapCanvas.tag_unbind(rr, '<Enter>')
            self.mapCanvas.itemconfig(t, text=info)
            self.mapCanvas.itemconfig(rr, tag='clicked')
            self.clickcounter(tag)
            # self.mapCanvas.addtag()

        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r

        rr = self.mapCanvas.create_oval(x0, y0, x1, y1, fill="green", tags=tag)
        t = self.mapCanvas.create_text(x + 20, y + 20, text="", tags=tag)#

        if "Distance" in info.split():
            showMessage()
            pass

        self.mapCanvas.tag_bind(rr, '<Button-1>', lambda event, tags=tag: dontHideMessage(tag))
        self.mapCanvas.tag_bind(rr, '<Enter>', lambda event: showMessage())
        self.mapCanvas.tag_bind(rr, '<Leave>', lambda event: hideMessage())

        return rr, t

    def loadButtons(self):

        for Points in self.intersections[::10]:

            x = Points[1] / 3
            y = Points[0] / 3
            t = str(Points)
            r = 5

            self.createPoint(x, y, r, t, "")

    def loadShortestPath(self, ppathList):
        for points in ppathList:
            x = points[1]/ 3
            y = points[0]/ 3
            r = 3
            t = "path"
            info = ""

            self.createPoint(x, y, r, t, info)

        pass


'''
this ths the gui handler
responsible for
function the create buttons
close window
dive tags?
enter
controlling two inputs
displaying text

'''
