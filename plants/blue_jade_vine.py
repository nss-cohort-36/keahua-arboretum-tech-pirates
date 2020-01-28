from plants import Plant

class Blue_Jade_Vine(Plant):
    def__init__(self):
        Plant.__init__(self, "Blue Jade Vine", "partial", 0, "Medium")
        self.add_location("Grassland") # need getter and setter for locations
        self.add_location("Swamp") # need getter and setter for locations