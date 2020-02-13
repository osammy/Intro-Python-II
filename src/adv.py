from room import Room
from player import Player
from inputParser import inputParser

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
initialRoom = room['outside']
player1 = Player('Samuel', initialRoom)
status = True


# Write a loop that:
#
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
def handleAction(actionType,game_player):
    if actionType == 'get' or actionType == 'take':
        return game_player.getItem
    elif actionType == 'drop':
        return game_player.dropItem
    # elif typedInput['actionType'] == 'move':
    #     return player1.move
    # elif typedInput['actionType'] == 'inventory' or typedInput['actionType'] == 'i':


    else: print("this case is not implememted")


while (status):

    # show items in room
    player1.printItemsInView()
    selection = input('\nSelect your movement: ')
    typedInput = inputParser(selection)
    if typedInput['err']:
        print(typedInput['msg'])
        continue

    if typedInput['actionType'] == 'move':
        status = player1.move(selection, room)
        continue
    elif typedInput['actionType'] == 'inventory' or typedInput['actionType'] == 'i':
        player1.getItems()
        continue

    handler = handleAction(typedInput['actionType'],player1)
    handler(typedInput['splittedInput'][1])

    continueGame = status
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
