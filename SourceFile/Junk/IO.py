class Program:
    def __init__(self, country):
        self.listOfPoints = []
        self.country = country
        self.t = open(self.getfilename(), "r")

    def getlist(self):
        #self.lines = self.t.readlines()
        try:
            for lines in self.t:
                for words in lines.split(", "):
                    words.replace(",\n", "")
                lines = lines.split(", ")
                row = int(lines[0])
                col = int(lines[1])
                text = lines[2].strip().replace(",", "")
                self.listOfPoints.append([(row, col), text])
        except ValueError:
            #continue
            pass #do nothing
        return self.listOfPoints


    def getfilename(self):
        if self.country == "es":
            return r'M:\22-23_CE301_olaoye_emmanuel_o\Algorithims\TextFiles\madridPoints'
        elif self.country == "fr":
            return r'M:\22-23_CE301_olaoye_emmanuel_o\Algorithims\TextFiles\parisPoints'
        elif self.country == "gb":
            return r'M:\22-23_CE301_olaoye_emmanuel_o\Algorithims\TextFiles\londonPoints'
        elif self.country == "us":
            return r'M:\22-23_CE301_olaoye_emmanuel_o\Algorithims\TextFiles\losangelesPoints'






# l = Program('us').getlist()
#
# for i in l:
#     print(i[0][0], i[0][1], i[1])