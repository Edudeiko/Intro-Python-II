from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [Item('Flash light', 'gives a bright light')]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
    falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('Sword', 'handy for defending yourself')]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Treasure chest', 'you are reach now!')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


new_player = Player('New Player', room['outside'])

print(f'Hello {new_player.name}!\nReady, set, go...')

while True:
    print(f'You are in {new_player.current_room.name}')
    print(new_player.current_room.description)
    if len(new_player.current_room.items) != 0:
        items_list = new_player.current_room.items.copy()
        for item in items_list:
            good_answer = False
            print(f"You found: {item.name}, {item.description}, lucky you...")
            while good_answer is False:
                answer = input('Do you want to pick up item? (y/n): ')
                if answer == 'y':
                    new_player.items.append(item)
                    new_player.current_room.items.remove(item)
                    good_answer = True
                elif answer == 'n':
                    good_answer = True
                else:
                    print('Please, choose yes or no!') 

        # player's inventory
        items_list = []
        for item in new_player.items:
            items_list.append(item.name)
        print(f'Your Inventory: {str(items_list)[1:-1]}')

        # for player to manage Items
        good_answer = False
        while good_answer is False:
            answer = input('Manage Inventory? (y/n): ')
            if answer == 'y':
                good_answer = True
                items_list = new_player.items.copy()
                for item in items_list:
                    remove_item = input(f'Remove {item.name}? (y/n): ')
                    if remove_item == 'y':
                        new_player.items.remove(item)
                        new_player.current_room.item.append(item)
                        item_list = []
                        for item in new_player.items:
                            item_list.append(item.name)
                        print(f'Your Inventory: {str(item_list)[1:-1]}')
                    elif remove_item == 'n':
                        pass
                    else:
                        pass
            elif answer == 'n':
                good_answer = True
            else:
                print('Please, choose yes or no!')

    # if room has no items
    else:
        print('No luck with items in this room...')
    direction = input('Which direction do you want to go next?\nPlease type: n, s, e, w or q to quit: ')
    if direction == 'n':
        try:
            new_player.current_room = new_player.current_room.n_to
        except:
            print('Oops, you hit a wall')
    if direction == 's':
        try:
            new_player.current_room = new_player.current_room.s_to
        except:
            print('Oops, you hit a wall')
    if direction == 'e':
        try:
            new_player.current_room = new_player.current_room.e_to
        except:
            print('Oops, you hit a wall')
    if direction == 'w':
        try:
            new_player.current_room = new_player.current_room.w_to
        except:
            print('Oops, you hit a wall')
    if direction == "stuff":
        item_list = []
        for item in new_player.items:
            item_list.append(item.name)
        print(f'Your Inventory: {str(item_list)[1:-1]}')
    if direction == 'q':
        break


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
