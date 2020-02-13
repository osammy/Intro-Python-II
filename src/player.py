# Write a class to hold player information, e.g. what room they are in
# currently.

import textwrap


class Player:

    directions = ['n','s','e','w','q']

    def __init__(self, name, room):
        self.name = name
        self.room = room
        # self.n_to, self.s_to, self.e_to, self.w_to = [
        #     None, None, None, None, None]

    def getPossibleNext(self):
        # A form of switch statement
        switcher = {
            'Outside Cave Entrance': {
                'n': "foyer"
            },
            'Foyer': {
                's': "outside",
                'n': "overlook",
                'e': "narrow"
            },
            'Grand Overlook': {
                's': "foyer"
            },
            'Narrow Passage': {
                'w': "foyer",
                'n': "treasure"
            },
            'Treasure Chamber': {
                's': "narrow"
            }
        }

        return switcher.get(self.room.name, {'errMsg': "Movement isn't allowed!"})

    def move(self, direction, rooms):
        if direction == 'q':
            print("\nGame Over\n")
            return False

        if direction not in self.directions:
            print(f"'{direction}' is an invalid selection, use any of these {self.directions}\n")
            return True


        next = self.getPossibleNext()
        roomKey = next.get(direction, 'Invalid Direction')

        if(roomKey == 'Invalid Direction'):
            print("That movement isn't allowed, try again.\n")
            return True
        
        print(f"ROOM NAME: {rooms[roomKey].name}\n")
        print(f"ROOM DESCRIPTION: {rooms[roomKey].description}\n")
        self.room = rooms[roomKey]
        return True
