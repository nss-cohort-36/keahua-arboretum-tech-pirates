from plants import Plant
from interfaces.identifiable import Identifiable

class Mountain_Apple_Tree(Plant, Identifiable):
    def__init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "partial", 17, "High")
        
        