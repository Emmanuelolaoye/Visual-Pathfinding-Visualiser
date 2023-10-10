isWall = []


class Node:
    def __call__(self, id):  # String id eg("5-5")
        self.id = id

    def get_x(self):
        return int(id.split("-")[0]) # not really needed right now as im not using web developement

    def get_y(self):
        return int(id.split("-")[0])

    def return_id(self):
        return f"current node is: {self.get_x()}-{self.get_y()}"

# for i in test:
#     for j in i:
#         # print(j)
#         for q in j:
#             print(q)