from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input('Enter player name: ')
player = Player('player_name', room['outside'])
print(f'New Adventure begins, {player.name}!')

# Write a loop that:
while True: 
# * Prints the current room name
    print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
# * Waits for user input and decides what to do.
    cmd = input('Choose a direction to move character: [n] North [s] South [e] East [w] West or [q] to exit game.')
    print(f'Going {cmd}!')
# If the user enters a cardinal direction, attempt to move to the room there.
    if len(cmd) == 1: 
        new_room = None
        if cmd in ['n', 's', 'e', 'w', 'q']:
            if cmd == 'n':
                new_room = player.current_room.n_to
            elif cmd == 's':
                new_room = player.current_room.s_to
            elif cmd == 'e':
                new_room = player.current_room.e_to
            elif cmd == 'w':
                new_room = player.current_room.w_to
            elif cmd == 'q':
                print('See you next time!')
                exit()
            if new_room: 
                player.current_room = new_room
            else:
                print('Cannot go this way ...')
        else: 
            print('ERROR: Invalid input')

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
