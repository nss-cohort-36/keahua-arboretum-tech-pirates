from .terrestrial import IsTerrestrial

class Foresty(IsTerrestrial):

    def __init__(self):
        super().__init__()
        self.foresty = True