# Write a class to hold player information, e.g. what room they are in
# currently.

import textwrap


class Player:

    def __init__(self, name, room):
        self.name = name
        self.current_room = room

    def getNext(self,direction):
        if direction == 'n':
            return self.current_room.n_to
        if direction == 's':
            return self.current_room.s_to
        if direction == 'e':
            return self.current_room.e_to
        if direction == 'w':
            return self.current_room.w_to

    def move(self, direction, rooms):
        if direction == 'q':
            print("\nGame Over\n")
            return False

        if hasattr(self.current_room,f'{direction}_to'):
            roomKey = None
            nextRoom = self.getNext(direction)
            for key, room in rooms.items():
                if room == nextRoom:
                    roomKey = key
            if roomKey == None:
                print('Invalid Movement')
                return True
            self.current_room = rooms[roomKey]
            print(f"ROOM NAME: {self.current_room.name}\n")
            print(f"ROOM DESCRIPTION: {self.current_room.description}\n")
        else: 
            print('invalid movement')
        
        return True
