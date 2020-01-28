from plants import Plant
from interfaces.identifiable import Identifiable

class Blue_Jade_Vine(Plant, Identifiable):
    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", "partial", 0, "Medium")
        