from plants import Plant

class Mountain_Apple_Tree(Plant):
    def__init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "partial", 17, "High")
        self.add_location("Mountain") # need getter and setter for locations
        