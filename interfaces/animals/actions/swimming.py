#****************************************************************************
# This file defines a specific action for an animal to inherit
#****************************************************************************

class IsSwimming:

    def __init__(self):
        self.swim_speed = 0
        self.maximum_depth = 0

    def swim(self):
        print("Glug glug, I'm swimming!")
