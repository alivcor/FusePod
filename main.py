# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from enum import Enum

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

class Nucleotide(object):
    def __init__(self, nucleobase, phosphate = "mono"):
        self.nucleobase = nucleobase
        self.phosphate = phosphate

    def canPair(self, nucleotide):
        return nucleotide.nucleobase in pairings[self.nucleobase]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adenine = Nucleotide(Nucleobase.A)
    guanine = Nucleotide(Nucleobase.G)
    uracil = Nucleotide(Nucleobase.U)
    print(adenine.canPair(guanine))
    print(adenine.canPair(uracil))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
