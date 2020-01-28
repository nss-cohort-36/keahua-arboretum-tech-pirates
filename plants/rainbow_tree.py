from plants import Plant
from interfaces import Identifiable

class RainbowTree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "full", 8, "low")
        Identifiable.__init__(self)