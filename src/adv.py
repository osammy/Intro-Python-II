from room import Room
from player import Player
from inputParser import inputParser
from color import color

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
def initPlayer():
    name = input("Enter Your Name: ")
    
    def basicSetup():
        roomOpts = ""
        count = 1
        len_of_keys = len(room.keys())
        print(f'\n{color.YELLOW} Select room options from 1 - {len_of_keys} {color.END}\n')
        for key in room:
            roomOpts += f'[{count}]: {key}    '
            count += 1
        print(color.BOLD + roomOpts + color.END)

        initial_room_by_index = int(input('Select any of the options: '))
        range_of_options = list(range(1, len_of_keys + 1))
        if initial_room_by_index not in range_of_options:
            print(f'{color.CYAN}Invalid option, please select any of {range_of_options} {color.END}')
            return basicSetup()
        else:
            roomKeys = list(room.keys())
            roomKey = roomKeys[initial_room_by_index]
            # Print welcome message
            print(f'\nWelcome {name}, to an amasing Maze Game.\n You are starting from {color.BOLD} {roomKey} {color.END} room')
    
            return Player(name,room[roomKey])

    return basicSetup()

player1 = initPlayer()
status = True


# Write a loop that:
#
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def handlePlay(typedInput,player):

    status = True

    if typedInput['err']:
        print(color.RED + typedInput['msg'] + color.END)
        return status

    if typedInput['actionType'] == 'move':
        status = player.move(selection, room)
        return status
    elif (typedInput['actionType'] == 'inventory') or (typedInput['actionType'] == 'i'):
        player.getItems()
    # Handle getting, taking actionTypes
    elif typedInput['actionType'] == 'get' or typedInput['actionType'] == 'take':
        itemName = typedInput['splittedInput'][1]
        player.getItem(itemName)
    elif typedInput['actionType'] == 'drop':
        itemName = typedInput['splittedInput'][1]
        player.dropItem(itemName)
    else:
        print('oops!, this shouldnt happen')
        # end the game abruptly
        status = False

    return status



while (status):
    # show items in room
    player1.printItemsInView()
    selection = input('\nSelect your action: ')
    # parse input and return formatted input plus do some checkings in input values
    typedInput = inputParser(selection)
    status = handlePlay(typedInput, player1)
    continueGame = status
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
