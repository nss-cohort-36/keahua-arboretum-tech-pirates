#****************************************************************************
# This file defines a specific action for an animal to inherit
#****************************************************************************

class IsWalking:

    def __init__(self, leg_count=2):
        self.leg_count = leg_count
        self.move_speed = 0
