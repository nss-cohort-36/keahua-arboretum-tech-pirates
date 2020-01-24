from .aquatic import IsAquatic

class IsSaltwater(IsAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "hypertonic"
