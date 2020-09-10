# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    '''Rooms in the game

    name and description attributes,
    The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    
    The `Room` class should be extended with a `list` that holds the `Item`s
    that are currently in that room.
    '''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
