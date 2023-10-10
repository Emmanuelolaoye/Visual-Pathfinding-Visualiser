"""
This a junkyard
containing unoptimised or
discarded ideas and functions

"""


# from tkinter import *
# from tkinter.tix import *
# import time
# from tkinter import messagebox, ttk
#
# from PIL import ImageTk, Image
# from SourceFile.computerVision import image
# # import guiHandler
#
#
# # Create an instance of tkinter window
# # win = Tk()
# # screenWidth = 1000
# # screenHeight = 800
# # win.geometry("%dx%d" % (screenWidth, screenHeight))
# # # win.attributes('-fullscreen', True)
# # win.resizable(False, False)
# #
# # bg = PhotoImage(file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Paris 40-2 1000x800.png")
#
#
# # frame = Frame(win, width=screenWidth, height=screenHeight)
# # frame.pack(fill=BOTH)
# #
# # # Show image using label
# # label1 = Label(win, image=bg)
# # label1.place(x=0, y=0)
# def hello():
#     print(hello)
#
#
# class MapWindow():
#     def __init__(self, frame, country):
#         self.frame = frame
#         self.country = country
#         self.counter = []
#         self.mapCanvas = Canvas(self.frame, width=1010, height=810)
#         self.loadCountryFrame()
#
#     def clickcounter(self, text):
#         self.counter.append(text)
#         if len(self.counter) == 2:
#             print(self.counter)
#             #hello()
#             self.counter.clear()
#
#     def destroyCanvas(self):
#         self.frame.destroy()
#         pass
#
#     def loadCountryFrame(self):
#         global backgoundImage
#         # self.destroyCanvas()
#
#         if self.country == "gb":
#             backgoundImage = self.getBackgroundImage()
#             mapCanvas = Canvas(self.frame, width=1010, height=810)
#             mapCanvas.pack()
#             mapCanvas.create_image(0, 0, anchor=NW, image=backgoundImage)
#             pass
#
#         elif self.country == "us":
#             backgoundImage = self.getBackgroundImage()
#             mapCanvas = Canvas(self.frame, width=1010, height=810)
#             mapCanvas.pack()
#             mapCanvas.create_image(0, 0, anchor=NW, image=backgoundImage)
#             pass
#
#         elif self.country == "fr":
#             backgoundImage = self.getBackgroundImage()
#
#             self.mapCanvas.pack()
#             self.mapCanvas.create_image(0, 0, anchor=NW, image=backgoundImage)
#
#             pass
#
#         elif self.country == "es":
#             backgoundImage = self.getBackgroundImage()
#             mapCanvas = Canvas(self.frame, width=1010, height=810)
#             mapCanvas.pack()
#             mapCanvas.create_image(0, 0, anchor=NW, image=backgoundImage)
#             pass
#
#         else:
#             return False
#
#     def getBackgroundImage(self):
#         if self.country == "gb":
#             return PhotoImage(file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\London 52-5 1000x800.png")
#
#         elif self.country == "us":
#             return PhotoImage(
#                 file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Los Angeles 78x10 1000x800.png")
#
#         elif self.country == "fr":
#             return PhotoImage(file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Paris 40-2 1000x800.png")
#
#         elif self.country == "es":
#             return PhotoImage(file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Madrid 34-2 1000x800.png")
#
#         else:
#             return False
#
#     # f = Frame(win, width=300, height=300, bg = 'blue')
#     #
#     # f.place(anchor='center', relx=0.5, rely=0.5)
#
#     def createPoint(self, x, y, r, canvas, tag, info):  # center coordinates, radius
#
#         def showMessage():
#             canvas.itemconfig(t, text=tag + " " + info)
#             canvas.itemconfig(rr, fill="blue")
#             # Get the bounding box of text
#             bbox = canvas.bbox(t)
#
#             # Outline the canvas text
#             rect = canvas.create_rectangle(bbox, outline="black", fill="white", tags="rect")
#             canvas.tag_raise(t, rect)
#
#         def hideMessage():
#             canvas.itemconfig(t, text="")
#             canvas.itemconfig(rr, fill="green")
#             canvas.delete("rect")
#
#         x0 = x - r
#         y0 = y - r
#         x1 = x + r
#         y1 = y + r
#
#         canvas.tag_bind(tag, '<Button-1>', lambda event, tags=tag: self.clickcounter(tags))
#         canvas.tag_bind(tag, '<Enter>', lambda event: showMessage())
#         canvas.tag_bind(tag, '<Leave>', lambda event: hideMessage())
#
#         rr = canvas.create_oval(x0, y0, x1, y1, fill="green", tags=tag)
#         t = canvas.create_text(x + 20, y + 20, text="", tags=tag)
#
#         return rr, t
#
#     def loadButtons(self):
#         if self.country == "fr":
#             self.createPoint(2591 / 3, 2202 / 3, 5, self.mapCanvas, "tag1", "info about tag1")
#
#
#
# ### Bin ####
#
# # mapCanvas = Canvas(win)
# # fr =PhotoImage(file=r"M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Paris 40-2 1000x800.png")
# # mapCanvas = Canvas(win, width=1010, height=810)
# # mapCanvas.pack()
# # mapCanvas.create_image(0, 0, anchor=NW, image=fr)
#
#
# # loadCountryFrame(win, "fr")
# # createPoint(2591 / 3, 2202 / 3, 5, mapCanvas, "tag1", "info about tag1")
# # Create an object of tkinter ImageTk
# # img = ImageTk.PhotoImage(Image.open())
#
# # Create a Label Widget to display the text or Image image=img
# # Label(f).pack(padx=0)
#
# # self.createPoint(2591 / 3, 2202 / 3, 5, mapCanvas, "tag1", "info about tag1")
# # #return mapCanvas
# # #button11 =
# # # button22 = createPoint((2591 / 3) / 2, (2202 / 3) / 2, 20, mapCanvas, "tag2", "info about tag2")
# # #return mapCanvas, button11
#
# # button = guiHandler.buttons(win)
# # button.loadbuttons()
#
#
# # win.mainloop()



# Import required libraries
from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
from SourceFile.Gui import GuiHandler, Graph
from SourceFile.computerVision import image
# import guiHandler
import concurrent.futures
import multiprocessing


# Create an instance of tkinter window

#
# f = Frame(win, width=300, height=300)
# f.pack()
# f.place(anchor='center', relx=0.5, rely=0.5)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open(image.get_image("map", 'London.png')))
#
# # Create a Label Widget to display the text or Image
# Label(f, image=img).pack(padx=0)
#
#
#
# separator = ttk.Separator(win, orient='vertical')
# separator.place(relx=0.2, rely=0, relwidth=0, relheight=1)
# Label(f, image=img).pack()
# #buttons.loadbuttons()


def getGraph(country):
    print(9875)
    if country == "es":
        Graph.Graph(spainGraph, country).getGraph()
    elif country == "fr":
        Graph.Graph(franceGraph, country).getGraph()
    elif country == "us":
        Graph.Graph(usaGraph, country).getGraph()
    elif country == "gb":
        Graph.Graph(gbGraph, country).getGraph()


# print("loading graphs")

# proceses = []
# countries = ["es", "fr", "gb", "us"]
# print(2222)
# for country in countries:
#     # print(country)
#     # p = multiprocessing.Process(target=getGraph, args=[country])
#     # p.start()
#     # proceses.append(p)
#     #
#     # for proceses in proceses:
#     #     proceses.join()
#     #
#     # # for procceses in concurrent.futures.as_completed(results):
#     # #     print(procceses.result())


def on_closing():
    if quitMessage.askokcancel("Quit", "Do you want to quit?"):
        win.destroy()


def goToLastPage(e):
    lastPage = pageTracker("last")
    if lastPage == "spain":
        spainChange('e')

    elif lastPage == "usa":
        USAChange('e')

    elif lastPage == "gb":
        gbChange('e')

    elif lastPage == "france":
        franceChange("e")


def pageTracker(newPage):
    if newPage == "last":
        return page[-1]
    else:
        page.append(newPage)


def spainChange(e):
    hideIndicator()
    spainImage = Image.open(r'\SourceFile\images\Buttons\Spain Flag.png').resize(
        (Map_selector1Width, Map_selector1Height), Image.Resampling.LANCZOS)
    newspainImage = ImageTk.PhotoImage(spainImage)
    spainLabel.config(image=newspainImage)
    spainLabel.image = newspainImage

    spainPage()


def spainChangeBack(e):
    spainImage = Image.open(r'\SourceFile\images\Maps\Madrid 34-2.png').resize(
        (Map_selector1Width, Map_selector1Height), Image.Resampling.LANCZOS)
    newspainImage = ImageTk.PhotoImage(spainImage)
    spainLabel.config(image=newspainImage)
    spainLabel.image = newspainImage


def gbChange(e):
    hideIndicator()
    gbImage = Image.open(r'\SourceFile\images\Buttons\GB Flag.png').resize(
        (Map_selector2Width, Map_selector2Height), Image.Resampling.LANCZOS)
    newGBimage = ImageTk.PhotoImage(gbImage)
    gbLabel.config(image=newGBimage)
    gbLabel.image = newGBimage
    gbPage()


def gbChangeBack(e):
    gbImage = Image.open(r'\SourceFile\images\Maps\London 52-5.png').resize(
        (Map_selector2Width, Map_selector2Height), Image.Resampling.LANCZOS)
    newGBimage = ImageTk.PhotoImage(gbImage)
    gbLabel.config(image=newGBimage)
    gbLabel.image = newGBimage


def USAChange(e):
    hideIndicator()
    USAImage = Image.open(r'\SourceFile\images\Buttons\USA Flag.png').resize(
        (Map_selector3Width, Map_selector3Height), Image.Resampling.LANCZOS)
    newUSAImage = ImageTk.PhotoImage(USAImage)
    USALabel.config(image=newUSAImage)
    USALabel.image = newUSAImage
    usaPage()


def USAChangeBack(e):
    USAImage = Image.open(r'\SourceFile\images\Maps\New York 43-10.png').resize(
        (Map_selector4Width, Map_selector4Height), Image.Resampling.LANCZOS)
    newUSAImage = ImageTk.PhotoImage(USAImage)
    USALabel.config(image=newUSAImage)
    USALabel.image = newUSAImage


def franceChange(e):
    hideIndicator()
    franceimage = Image.open(r'\SourceFile\images\Buttons\France Flag.png').resize(
        (Map_selector3Width, Map_selector3Height), Image.Resampling.LANCZOS)
    newFranceImage = ImageTk.PhotoImage(franceimage)
    franceLabel.config(image=newFranceImage)
    franceLabel.image = newFranceImage

    francePage()


def franceChangeBack(e):
    franceimage = Image.open(r'\SourceFile\images\Maps\Paris 52-5.png').resize(
        (Map_selector3Width, Map_selector3Height), Image.Resampling.LANCZOS)
    newFranceImage = ImageTk.PhotoImage(franceimage)
    franceLabel.config(image=newFranceImage)
    franceLabel.image = newFranceImage


def destroyFrameChildren(frame):
    # destroys all widgets from Mapframe
    for widgets in frame.winfo_children():
        widgets.destroy()


# makes sure only the most recent button shows the flag
def hideIndicator():
    franceChangeBack(0)
    spainChangeBack(0)
    USAChangeBack(0)
    gbChangeBack(0)

    destroyFrameChildren(map_frame)


def spainPage():
    # spainImageMap = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Madrid 34-2.png').resize(
    #     (1100, 800), Image.Resampling.LANCZOS)
    # newspainImageMap = ImageTk.PhotoImage(spainImageMap)
    # spainLabelMap = Label(map_frame, image=newspainImageMap)
    # spainLabelMap.place(relx=.5, rely=0.5, anchor='c')
    # spainLabelMap.config(image=newspainImageMap)
    # spainLabelMap.image = newspainImageMap
    spain = GuiHandler.MapWindow(map_frame, "es")
    # todo insert get graph function here`
    spain.loadButtons()
    pass


def gbPage():
    # gbImageMap = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\London 52-5.png').resize(
    #     (1100, 800), Image.Resampling.LANCZOS)
    # newGBimageMap = ImageTk.PhotoImage(gbImageMap)
    # gbLabelMap = Label(map_frame, image=newGBimageMap)
    # gbLabelMap.place(relx=.5, rely=0.5, anchor='c')
    # gbLabelMap.config(image=newGBimageMap)
    # gbLabelMap.image = newGBimageMap
    gb = GuiHandler.MapWindow(map_frame, "gb")
    # todo insert get graph function here
    gb.loadButtons()
    pass


def usaPage():
    # USAImageMap = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\New York 43-10.png').resize(
    #     (1100, 800), Image.Resampling.LANCZOS)
    # newUSAImageMap = ImageTk.PhotoImage(USAImageMap)
    # USALabelMap = Label(map_frame, image=newUSAImageMap)
    # USALabelMap.place(relx=.5, rely=0.5, anchor='c')
    # USALabelMap.config(image=newUSAImageMap)
    # USALabelMap.image = newUSAImageMap
    GuiHandler.MapWindow(map_frame, "us")
    # todo insert get graph function here
    pass


def francePage():
    # franceimageMap = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Paris 52-5.png').resize(
    #     (1100, 800), Image.Resampling.LANCZOS)
    # newFranceImageMap = ImageTk.PhotoImage(franceimageMap)
    # franceLabelMap = Label(map_frame, image=newFranceImageMap)
    # franceLabelMap.place(relx=.5, rely=0.5, anchor='c')
    # franceLabelMap.config(image=newFranceImageMap)
    # franceLabelMap.image = newFranceImageMap
    france = GuiHandler.MapWindow(map_frame, "fr")
    # todo insert get graph function here
    france.loadButtons()

    pass


def spainHover(e):
    spainLabel.config(font=("Courier", 50, "bold"))


def spainNoHover(e):
    spainLabel.config(font=("Courier", 30, "bold"))


def gbHover(e):
    gbLabel.config(font=("Courier", 50, "bold"))


def gbNoHover(e):
    gbLabel.config(font=("Courier", 30, "bold"))


def usaHover(e):
    USALabel.config(font=("Courier", 40, "bold"))


def usaNoHover(e):
    USALabel.config(font=("Courier", 30, "bold"))


def franceHover(e):
    franceLabel.config(font=("Courier", 50, "bold"))


def franceNoHover(e):
    franceLabel.config(font=("Courier", 30, "bold"))


page = []
franceGraph = {}
usaGraph = {}
gbGraph = {}
spainGraph = {}

win = Tk()
screenWidth = 1440
screenHeight = 900
win.geometry("%dx%d" % (screenWidth, screenHeight))
# win.attributes('-fullscreen', True)
win.resizable(False, False)

# buttons = guiHandler.buttons(win)
quitMessage = messagebox

left_frame = Frame(win, width=288, height=screenHeight, bg="#121212")
left_frame.grid(row=0, column=0, padx=0, pady=0)
left_frame.grid_propagate(False)  # stops frma from shrinking in size

right_frame = Frame(win, width=(screenWidth - 288), height=screenHeight, bg="#121212")  # , bg="#57BE46"
right_frame.grid(row=0, column=1, padx=0, pady=0)

map_frame = Frame(right_frame, width=(screenWidth - 288), height=(screenHeight - 90), bg="#121212")  #
menu_bar = Frame(right_frame, width=(screenWidth - 288), height=90, bg="#282828")

map_frame.grid(row=0, column=0)
menu_bar.grid(row=1, column=0, sticky="s")

map_frame.update()

mapw = map_frame.winfo_width()
maph = map_frame.winfo_height()

Map_selector1 = Frame(left_frame, width=266, height=150)  # , bg="#B6C16D"
Map_selector1.grid(row=0, column=0, padx=10, pady=15, sticky="n")
Map_selector1.update()
Map_selector1Width = Map_selector1.winfo_width()
Map_selector1Height = Map_selector1.winfo_height()

spainImage = Image.open(r'\SourceFile\images\Maps\Madrid 34-2.png').resize(
    (Map_selector1.winfo_width(), Map_selector1.winfo_height()), Image.Resampling.LANCZOS)
# resizedSpainImage = spainImage
newspainImage = ImageTk.PhotoImage(spainImage)
spainLabel = Label(Map_selector1, text='Madrid', image=newspainImage, compound='center', font=("Courier", 40, "bold"))
spainLabel.pack()

Map_selector2 = Frame(left_frame, width=266, height=150, bg="#92C16D")
Map_selector2.grid(row=1, column=0, padx=10, pady=15, sticky="n")
Map_selector2.update()
Map_selector2Width = Map_selector2.winfo_width()
Map_selector2Height = Map_selector2.winfo_height()

# pack GB FLag onto Map_selector2 Frame
gbImage = Image.open(r'\SourceFile\images\Maps\London 52-5.png').resize(
    (Map_selector2.winfo_width(), Map_selector2.winfo_height()), Image.Resampling.LANCZOS)
newGBimage = ImageTk.PhotoImage(gbImage)
gbLabel = Label(Map_selector2, text='London', image=newGBimage, compound='center', font=("Courier", 40, "bold"))
gbLabel.pack()

Map_selector3 = Frame(left_frame, width=266, height=150, bg="#6D94C1")
Map_selector3.grid(row=2, column=0, padx=10, pady=15, sticky="n")
Map_selector3.update()
Map_selector3Width = Map_selector3.winfo_width()
Map_selector3Height = Map_selector3.winfo_height()

franceimage = Image.open(r'\SourceFile\images\Maps\Paris 52-5.png').resize(
    (Map_selector3.winfo_width(), Map_selector3.winfo_height()), Image.Resampling.LANCZOS)
newFranceImage = ImageTk.PhotoImage(franceimage)
franceLabel = Label(Map_selector3, text='Paris', image=newFranceImage, compound='center', font=("Courier", 40, "bold"))
franceLabel.pack()

Map_selector4 = Frame(left_frame, width=266, height=150, bg="#AB6DC1")
Map_selector4.grid(row=3, column=0, padx=10, pady=15, sticky="n")
Map_selector4.update()
Map_selector4Width = Map_selector4.winfo_width()
Map_selector4Height = Map_selector4.winfo_height()

USAImage = Image.open(r'\SourceFile\images\Maps\New York 43-10.png').resize(
    (Map_selector4.winfo_width(), Map_selector4.winfo_height()), Image.Resampling.LANCZOS)
newUSAImage = ImageTk.PhotoImage(USAImage)
USALabel = Label(Map_selector4, text='New York', image=newUSAImage, compound='center', font=("Courier", 35, "bold"))
USALabel.pack()

# Binding  when the buton is hovered over, it will change the image to its respective flag and change back then the mouse leave
spainLabel.bind('<Button-1>', spainChange)
spainLabel.bind('<Enter>', spainHover)
spainLabel.bind('<Leave>', spainNoHover)
# spainLabel.bind('<Button-1>', indicateSpain)

gbLabel.bind('<Button-1>', gbChange)
gbLabel.bind('<Enter>', gbHover)
gbLabel.bind('<Leave>', gbNoHover)

# gbLabel.bind('<Leave>', gbChangeBack)

USALabel.bind('<Button-1>', USAChange)
USALabel.bind('<Enter>', usaHover)
USALabel.bind('<Leave>', usaNoHover)

# USALabel.bind('<Leave>', USAChangeBack)

franceLabel.bind('<Button-1>', franceChange)
franceLabel.bind('<Enter>', franceHover)
franceLabel.bind('<Leave>', franceNoHover)
# franceLabel.bind('<Leave>', franceChangeBack)

# todo make a new button and add all features like click etc

# print(mapw, maph)

win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()


def hello():
    print(hello)


class Buttons:

    def __init__(self, win):
        self.win = win
        self.counter = []

    def clickcounter(self, text):
        self.counter.append(text)
        if len(self.counter) == 2:
            print(self.counter)
            hello()
            self.counter.clear()

    def loadButtons(self):
        button1 = Button(self.win, text="button1", command=lambda idx='button1': self.clickcounter(idx))
        button2 = Button(self.win, text="button2", command=lambda idx='button2': self.clickcounter(idx))
        button3 = Button(self.win, text="button3", command=lambda idx='button3': self.clickcounter(idx))
        button4 = Button(self.win, text="button4", command=lambda idx='button4': self.clickcounter(idx))
        button5 = Button(self.win, text="button5", command=lambda idx='button5': self.clickcounter(idx))
        button6 = Button(self.win, text="button6", command=lambda idx='button6': self.clickcounter(idx))
        button7 = Button(self.win, text="button7", command=lambda idx='button7': self.clickcounter(idx))

        button1.place(x=110, y=235)
        button2.place(x=150, y=160)
        button3.place(x=300, y=160)
        button4.place(x=340, y=235)
        button5.place(x=300, y=310)
        button6.place(x=150, y=310)
        button7.place(x=225, y=235)

    def pressed(self, w):
        pass

