from interfaces.animals.terrestrial import IsTerrestrial

class Grasslandy(IsTerrestrial):
    
    def __init__(self):
        super().__init__()
        self.grasslandy = True