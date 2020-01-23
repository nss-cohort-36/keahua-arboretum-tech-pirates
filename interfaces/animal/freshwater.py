from interfaces.aquatic import IAquatic
# Error 1 solving Circular Import due to import path being without direction to aquatic. Example: from aquatic import IAquatic
# Solution from interfaces.aquatic import IAquatic
class IFreshwater(IAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "hypertonic"
