import random

from constants import *
from main import *
import collections

class WorldNode(object):
    def __init__(self, x, y, elements=set(), h=1):
        self.locationX = x
        self.locationY = y
        self.elements = set()
        self.habitablity = h  # -5 (least habitable) to 5 (most habitable)

    def __repr__(self):
        return "[(X: {}, Y: {}), [{}], H: {}]".format(self.locationX, self.locationY, self.elements, self.habitablity)


def getRandomNode(i, j):
    node = WorldNode(i, j, set(), random.randint(-5, 5))
    return node


def getRandomNucleotide():
    bases = [Nucleobase.A, Nucleobase.C, Nucleobase.G, Nucleobase.T, Nucleobase.U]
    return Nucleotide(bases[random.randint(0, 4)])


class World(object):
    def __init__(self, n):
        self.n = n
        self.grid = [[getRandomNode(i, j) for j in range(n)] for i in range(n)]

    def __repr__(self):
        rep = ""
        for row in self.grid:
            rep += "\n" + str(row)
        return rep

    def flourish(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].habitablity > MIN_HABITABILITY and random.randint(0, 10) > 7:
                    self.grid[i][j].elements.add(getRandomNucleotide())

    def nextState(self):
        newState = [[self.grid[i][j] for j in range(self.n)] for i in range(self.n)]
        def bfs(i, j):

            q = collections.deque()
            q.append(self.grid[i][j])
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]
            visited = dict()
            visited[(i,j)] = True

            while q:
                node = q.popleft()

                for _dir in dirs:
                    nei_loc = (node.locationX + _dir[0],node.locationY + _dir[1])
                    if nei_loc[0] < 0 or nei_loc[1] < 0 or nei_loc[0] >= len(self.grid) or nei_loc[1] >= len(self.grid[0]) or nei_loc in visited or self.grid[nei_loc[0]][nei_loc[1]].habitablity < MIN_HABITABILITY:
                        continue
                    else:
                        nei = self.grid[nei_loc[0]][nei_loc[1]]
                        visited[nei] = True



            # for element in self.grid[i][j].elements:
            #     if element.getCompoundType() == "Nucleotide" and newState[si][sj] == "Nucleotide":
            #         newState[si][sj].


            return
    #
    # for i in range(len(self.grid)):
    #     for j in range(len(self.grid[0])):
    #         if len(self.grid[i][j].elements) > 0:
    #             dfs(i,j,i,j)
