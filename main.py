# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from enum import Enum
from abc import ABC, abstractmethod
from world import *


class OrganicCompound(ABC):
    def __init__(self):
        self.mobility = Mobility.NORMAL

    @classmethod
    def getCompoundType(cls):
        return cls.__name__



class Mobility(Enum):
    VERY_HIGH = 3
    HIGH = 2
    NORMAL = 1
    ZERO = 0


class Nucleobase(Enum):
    A = "Adenine"
    C = "Cytosine"
    G = "Guanine"
    T = "Thymine"
    U = "Uracil"


pairings = {
    Nucleobase.A: (Nucleobase.U, Nucleobase.T),
    Nucleobase.C: (Nucleobase.G),
    Nucleobase.G: (Nucleobase.C),
    Nucleobase.T: (Nucleobase.A),
    Nucleobase.U: (Nucleobase.A)
}


class RNA(OrganicCompound):
    def __init__(self, nucleotides):
        super().__init__()
        self.nucleotides = tuple(nucleotides)  # ()
        # self.mobility =

    def __repr__(self):
        return "-".join([str(nucleotide.nucleobase) for nucleotide in self.nucleotides])



class Nucleotide(OrganicCompound):
    def __init__(self, nucleobase, phosphate="mono"):
        super().__init__()
        self.nucleobase = nucleobase
        self.phosphate = phosphate

    def canBond(self, nucleotide):
        return nucleotide.nucleobase in pairings[self.nucleobase]

    def pair(self, nucleotide):
        return RNA([self, nucleotide])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adenine = Nucleotide(Nucleobase.A)
    guanine = Nucleotide(Nucleobase.G)
    uracil = Nucleotide(Nucleobase.U)
    print(adenine.canBond(guanine))
    print(adenine.canBond(uracil))

    world = World(50)
    world.flourish()

    print(world)

    print(adenine.pair(guanine).getCompoundType())
    print(adenine.pair(guanine).mobility)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
