from .terrestrial import IsTerrestrial

    class Mountainy(IsTerrestrial):
        # Using super(type[, object-or-type]) to get access to the type in release_animal. Going to override class to be able to use isinstance to check for type that i am settin up here.
        def__init__(self):
            super().__init__()
            self.mountainy = True
            
        # Super only works with new style classes. Can also be used by getattr() and allows dynamic use any time inheritance is updated