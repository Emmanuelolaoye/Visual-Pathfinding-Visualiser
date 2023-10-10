# Import required libraries
# from tkinter import *
import warnings
from tkinter import messagebox, ttk, Canvas, PhotoImage, Button, Frame, Label
from PIL import ImageTk, Image
from SourceFile.Gui import GuiHandler, Graph
# import guiHandler




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


class GUI:
    def __init__(self, win, listOfGraphs):
        self.win = win
        self.page = []
        self.listOfGraphs = listOfGraphs  # todo make it do something


        self.spainGraph = self.getgraphindex('ES')[0]
        self.franceGraph = self.getgraphindex('FR')[0]
        self.gbGraph = self.getgraphindex('GB')[0]
        self.usaGraph = self.getgraphindex('US')[0]


        self.spainintersections = self.getgraphindex('ES')[1]
        self.franceintersections = self.getgraphindex('FR')[1]
        self.gbintersections = self.getgraphindex('GB')[1]
        self.usaintersections = self.getgraphindex('US')[1]


        self.screenWidth = 1440
        self.screenHeight = 900
        self.win.configure(background='black')
        self.win.geometry("%dx%d" % (self.screenWidth, self.screenHeight))
        # win.attributes('-fullscreen', True)
        self.win.resizable(False, False)

        # buttons = guiHandler.buttons(win)
        self.quitMessage = messagebox

        self.left_frame = Frame(win, width=288, height=self.screenHeight, bg="#121212")
        self.left_frame.grid(row=0, column=0, padx=0, pady=0)
        self.left_frame.grid_propagate(False)  # stops frma from shrinking in size

        self.right_frame = Frame(win, width=(self.screenWidth - 288), height=self.screenHeight,
                                 bg="#121212")  # , bg="#57BE46"
        self.right_frame.grid(row=0, column=1, padx=0, pady=0)

        self.map_frame = Frame(self.right_frame, width=(self.screenWidth - 288), height=(self.screenHeight - 90),
                               bg="#121212")  #
        self.menu_bar = Frame(self.right_frame, width=(self.screenWidth - 288), height=90, bg="#121212")

        self.map_frame.grid(row=0, column=0)
        self.menu_bar.grid(row=1, column=0, sticky="s")

        self.map_frame.update()

        self.mapw = self.map_frame.winfo_width()
        self.maph = self.map_frame.winfo_height()

        self.Map_selector1 = Frame(self.left_frame, width=266, height=150)  # , bg="#B6C16D"
        self.Map_selector1.grid(row=0, column=0, padx=10, pady=15, sticky="n")
        self.Map_selector1.update()
        self.Map_selector1Width = self.Map_selector1.winfo_width()
        self.Map_selector1Height = self.Map_selector1.winfo_height()

        self.spainImage = Image.open(
            r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Madrid 34-2.png').resize(
            (self.Map_selector1.winfo_width(), self.Map_selector1.winfo_height()), Image.Resampling.LANCZOS)
        # resizedSpainImage = spainImage
        self.newspainImage = ImageTk.PhotoImage(self.spainImage)
        self.spainLabel = Label(self.Map_selector1, text='Madrid', image=self.newspainImage, compound='center',
                                font=("Courier", 40, "bold"))
        self.spainLabel.pack()

        self.Map_selector2 = Frame(self.left_frame, width=266, height=150, bg="#92C16D")
        self.Map_selector2.grid(row=1, column=0, padx=10, pady=15, sticky="n")
        self.Map_selector2.update()
        self.Map_selector2Width = self.Map_selector2.winfo_width()
        self.Map_selector2Height = self.Map_selector2.winfo_height()

        # pack GB FLag onto Map_selector2 Frame
        self.gbImage = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\London 52-5.png').resize(
            (self.Map_selector2.winfo_width(), self.Map_selector2.winfo_height()), Image.Resampling.LANCZOS)
        self.newGBimage = ImageTk.PhotoImage(self.gbImage)
        self.gbLabel = Label(self.Map_selector2, text='London', image=self.newGBimage, compound='center',
                             font=("Courier", 40, "bold"))
        self.gbLabel.pack()

        self.Map_selector3 = Frame(self.left_frame, width=266, height=150, bg="#6D94C1")
        self.Map_selector3.grid(row=2, column=0, padx=10, pady=15, sticky="n")
        self.Map_selector3.update()
        self.Map_selector3Width = self.Map_selector3.winfo_width()
        self.Map_selector3Height = self.Map_selector3.winfo_height()

        self.franceimage = Image.open(
            r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Paris 52-5.png').resize(
            (self.Map_selector3.winfo_width(), self.Map_selector3.winfo_height()), Image.Resampling.LANCZOS)
        self.newFranceImage = ImageTk.PhotoImage(self.franceimage)
        self.franceLabel = Label(self.Map_selector3, text='Paris', image=self.newFranceImage, compound='center',
                                 font=("Courier", 40, "bold"))
        self.franceLabel.pack()

        self.Map_selector4 = Frame(self.left_frame, width=266, height=150, bg="#AB6DC1")
        self.Map_selector4.grid(row=3, column=0, padx=10, pady=15, sticky="n")
        self.Map_selector4.update()
        self.Map_selector4Width = self.Map_selector4.winfo_width()
        self.Map_selector4Height = self.Map_selector4.winfo_height()

        self.USAImage = Image.open(
            r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Los Angeles 78x10 1000x800.png').resize(
            (self.Map_selector4.winfo_width(), self.Map_selector4.winfo_height()), Image.Resampling.LANCZOS)
        self.newUSAImage = ImageTk.PhotoImage(self.USAImage)
        self.USALabel = Label(self.Map_selector4, text='Las Angeles', image=self.newUSAImage, compound='center',
                              font=("Courier", 25, "bold"))
        self.USALabel.pack()

        self.clearAllButton = Button(self.left_frame, text="Clear All", bg='white', command=lambda: self.goToLastPage())
        self.clearAllButton.grid(row=4, column=0, padx=10, pady=15, sticky="n")

        # Binding  when the buton is hovered over, it will change the image to its respective flag and change back then the mouse leave
        self.spainLabel.bind('<Button-1>', self.spainChange)
        self.spainLabel.bind('<Enter>', self.spainHover)
        self.spainLabel.bind('<Leave>', self.spainNoHover)
        # spainLabel.bind('<Button-1>', indicateSpain)

        self.gbLabel.bind('<Button-1>', self.gbChange)
        self.gbLabel.bind('<Enter>', self.gbHover)
        self.gbLabel.bind('<Leave>', self.gbNoHover)

        # gbLabel.bind('<Leave>', gbChangeBack)

        self.USALabel.bind('<Button-1>', self.USAChange)
        self.USALabel.bind('<Enter>', self.usaHover)
        self.USALabel.bind('<Leave>', self.usaNoHover)

        # USALabel.bind('<Leave>', USAChangeBack)

        self.franceLabel.bind('<Button-1>', self.franceChange)
        self.franceLabel.bind('<Enter>', self.franceHover)
        self.franceLabel.bind('<Leave>', self.franceNoHover)
        self.win.protocol("WM_DELETE_WINDOW", self.on_closing)
        # franceLabel.bind('<Leave>', franceChangeBack)

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

    def on_closing(self):
        if self.quitMessage.askokcancel("Quit", "Do you want to quit?"):
            self.win.destroy()

    def goToLastPage(self):
        try:
            lastPage = self.pageTracker("last")
            if lastPage == "spain":
                self.spainChange(0)

            elif lastPage == "usa":
                self.USAChange(0)

            elif lastPage == "gb":
                self.gbChange(0)

            elif lastPage == "france":
                self.franceChange(0)
        except Exception:
            messagebox.showinfo("Error", "Please select a country First")

    def pageTracker(self, newPage):
        if newPage == "last":
            return self.page[-1]
        else:
            self.page.append(newPage)

    def spainChange(self, e):
        self.hideIndicator()
        self.pageTracker("spain")
        print(self.page)
        self.spainImage = Image.open(
            r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Buttons\Spain Flag.png').resize(
            (self.Map_selector1Width, self.Map_selector1Height), Image.Resampling.LANCZOS)
        self.newspainImage = ImageTk.PhotoImage(self.spainImage)
        self.spainLabel.config(image=self.newspainImage)
        self.spainLabel.image = self.newspainImage

        self.spainPage()

    def spainChangeBack(self, e):
        self.spainImage = Image.open(
            r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Madrid 34-2.png').resize(
            (self.Map_selector1Width, self.Map_selector1Height), Image.Resampling.LANCZOS)
        self.newspainImage = ImageTk.PhotoImage(self.spainImage)
        self.spainLabel.config(image=self.newspainImage)
        self.spainLabel.image = self.newspainImage

    def gbChange(self, e):
        self.hideIndicator()
        self.pageTracker("gb")
        print(self.page)
        self.gbImage = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Buttons\GB Flag.png').resize(
            (self.Map_selector2Width, self.Map_selector2Height), Image.Resampling.LANCZOS)
        self.newGBimage = ImageTk.PhotoImage(self.gbImage)
        self.gbLabel.config(image=self.newGBimage)
        self.gbLabel.image = self.newGBimage
        self.gbPage()

    def gbChangeBack(self, e):
        self.gbImage = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\London 52-5.png').resize(
            (self.Map_selector2Width, self.Map_selector2Height), Image.Resampling.LANCZOS)
        self.newGBimage = ImageTk.PhotoImage(self.gbImage)
        self.gbLabel.config(image=self.newGBimage)
        self.gbLabel.image = self.newGBimage

    def USAChange(self, e):
        self.hideIndicator()
        self.pageTracker("usa")
        print(self.page)
        self.USAImage = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Buttons\USA Flag.png').resize(
            (self.Map_selector3Width, self.Map_selector3Height), Image.Resampling.LANCZOS)
        self.newUSAImage = ImageTk.PhotoImage(self.USAImage)
        self.USALabel.config(image=self.newUSAImage)
        self.USALabel.image = self.newUSAImage
        self.usaPage()

    def USAChangeBack(self, e):
        self.USAImage = Image.open(
            r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Los Angeles 78x10 1000x800.png').resize(
            (self.Map_selector4Width, self.Map_selector4Height), Image.Resampling.LANCZOS)
        newUSAImage = ImageTk.PhotoImage(self.USAImage)
        self.USALabel.config(image=newUSAImage)
        self.USALabel.image = newUSAImage

    def franceChange(self, e):
        self.hideIndicator()
        self.pageTracker("france")
        print(self.page)
        self.franceimage = Image.open(
            r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Buttons\France Flag.png').resize(
            (self.Map_selector3Width, self.Map_selector3Height), Image.Resampling.LANCZOS)
        self.newFranceImage = ImageTk.PhotoImage(self.franceimage)
        self.franceLabel.config(image=self.newFranceImage)
        self.franceLabel.image = self.newFranceImage

        self.francePage()

    def franceChangeBack(self, e):
        self.franceimage = Image.open(
            r'M:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Paris 52-5.png').resize(
            (self.Map_selector3Width, self.Map_selector3Height), Image.Resampling.LANCZOS)
        self.newFranceImage = ImageTk.PhotoImage(self.franceimage)
        self.franceLabel.config(image=self.newFranceImage)
        self.franceLabel.image = self.newFranceImage

    def destroyFrameChildren(self, frame):
        # destroys all widgets from Mapframe
        for widgets in frame.winfo_children():
            widgets.destroy()

    # makes sure only the most recent button shows the flag
    def hideIndicator(self):
        self.franceChangeBack(0)
        self.spainChangeBack(0)
        self.USAChangeBack(0)
        self.gbChangeBack(0)

        self.destroyFrameChildren(self.map_frame)

    def getgraphindex(self, country):
        countryGraph = self.listOfGraphs.index(country) + 1
        countryIntersections = self.listOfGraphs.index(country) + 2

        return self.listOfGraphs[countryGraph], self.listOfGraphs[countryIntersections]

    def spainPage(self):
        # spainImageMap = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_oM:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Madrid 34-2.png').resize(
        #     (1100, 800), Image.Resampling.LANCZOS)
        # newspainImageMap = ImageTk.PhotoImage(spainImageMap)
        # spainLabelMap = Label(map_frame, image=newspainImageMap)
        # spainLabelMap.place(relx=.5, rely=0.5, anchor='c')
        # spainLabelMap.config(image=newspainImageMap)
        # spainLabelMap.image = newspainImageMap

        spain = GuiHandler.MapWindow(self.map_frame, "es", self.spainGraph, self.spainintersections)
        # todo insert get graph function here`
        spain.loadButtons()
        pass

    def gbPage(self):
        # gbImageMap = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_oM:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\London 52-5.png').resize(
        #     (1100, 800), Image.Resampling.LANCZOS)
        # newGBimageMap = ImageTk.PhotoImage(gbImageMap)
        # gbLabelMap = Label(map_frame, image=newGBimageMap)
        # gbLabelMap.place(relx=.5, rely=0.5, anchor='c')
        # gbLabelMap.config(image=newGBimageMap)
        # gbLabelMap.image = newGBimageMap
        gb = GuiHandler.MapWindow(self.map_frame, "gb", self.gbGraph, self.gbintersections)
        # todo insert get graph function here
        gb.loadButtons()
        pass

    def usaPage(self):
        # USAImageMap = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_oM:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\New York 43-10.png').resize(
        #     (1100, 800), Image.Resampling.LANCZOS)
        # newUSAImageMap = ImageTk.PhotoImage(USAImageMap)
        # USALabelMap = Label(map_frame, image=newUSAImageMap)
        # USALabelMap.place(relx=.5, rely=0.5, anchor='c')
        # USALabelMap.config(image=newUSAImageMap)
        # USALabelMap.image = newUSAImageMap
        #graph = self.usaGraph
        us = GuiHandler.MapWindow(self.map_frame, "us", self.usaGraph, self.usaintersections)
        us.loadButtons()
        #print(graph)
        pass

    def francePage(self):
        # franceimageMap = Image.open(r'M:\22-23_CE301_olaoye_emmanuel_oM:\22-23_CE301_olaoye_emmanuel_o\SourceFile\images\Maps\Paris 52-5.png').resize(
        #     (1100, 800), Image.Resampling.LANCZOS)
        # newFranceImageMap = ImageTk.PhotoImage(franceimageMap)
        # franceLabelMap = Label(map_frame, image=newFranceImageMap)
        # franceLabelMap.place(relx=.5, rely=0.5, anchor='c')
        # franceLabelMap.config(image=newFranceImageMap)
        # franceLabelMap.image = newFranceImageMap
        france = GuiHandler.MapWindow(self.map_frame, "fr", self.franceGraph, self.franceintersections)
        # todo insert get graph function here
        france.loadButtons()

        pass

    def spainHover(self, e):
        self.spainLabel.config(font=("Courier", 50, "bold"))

    def spainNoHover(self, e):
        self.spainLabel.config(font=("Courier", 30, "bold"))

    def gbHover(self, e):
        self.gbLabel.config(font=("Courier", 50, "bold"))

    def gbNoHover(self, e):
        self.gbLabel.config(font=("Courier", 30, "bold"))

    def usaHover(self, e):
        self.USALabel.config(font=("Courier", 30, "bold"))

    def usaNoHover(self, e):
        self.USALabel.config(font=("Courier", 25, "bold"))

    def franceHover(self, e):
        self.franceLabel.config(font=("Courier", 50, "bold"))

    def franceNoHover(self, e):
        self.franceLabel.config(font=("Courier", 30, "bold"))

    # todo make a new button and add all features like click etc

    # print(mapw, maph)
