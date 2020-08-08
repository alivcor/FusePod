import random

class WorldNode(object):
    def __init__(self, x, y, elements = set(), h = 1):
        self.locationX = x
        self.locationY = y
        self.elements = set()
        self.habitablity = h # -5 (least habitable) to 5 (most habitable)

    def __repr__(self):
        return "[(X: {}, Y: {}), [{}], H: {}]".format(self.locationX, self.locationY, self.elements, self.habitablity)

def getRandomNode(i,j):
    node = WorldNode(i,j,set(),random.randint(-5,5))
    return node

class World:
    def __init__(self, n):
        self.grid = [[getRandomNode(i,j) for j in range(n)] for i in range(n)]

    def __repr__(self):
        rep = ""
        for row in self.grid:
            rep += "\n" + str(row)
        return rep


