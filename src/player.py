# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    '''Players should have a name, current_room attributes
    '''
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        # self.items = {}
        self.items = items

    def __str__(self):
        return f'{self.name.title()}\n{self.__dict__}'

    def move(self, *args):
        '''To move Player from one room to another
        '''
        if not args[0]:
            print('Please specify where do you want to move next \n')
            print('Valid commands are `n`, `s`, `e` and `w` which move the player North, South, East or West \n')
            print('For example to move South type -> "move s" \n')
            return
        command_to_move = args[0][0]
        if command_to_move in ['n', 's', 'e', 'w']:
            good_move = eval(f'self.current_room.to{command_to_move}')
            if good_move:
                self.current_room.characters.pop(self.name, None)
                self.current_room = good_move
                self.current_room.characters[self.name] = self
                self.current_position()
            else:
                directions = {'n': 'North', 's': 'South', 'w': 'West', 'e': 'East'}
                print(f'Can not go to {directions[command_to_move]}. \n')

    def current_position(self):
        '''Prints current room and room's description'''
        print(f'{self.current_room.name} \n{self.current_room.description} \n')
