from plants import Plant
from interfaces import Identifiable

class Silversword(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Silversword", "shade", 22, "high")
        Identifiable.__init__(self)