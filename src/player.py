# Write a class to hold player information, e.g. what room they are in
# currently.

import textwrap
from room import Room
from item import Item
from color import color

class Player(Room):

    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        self.items = []

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
            # print("\033[0;37;40m Normal text\n")
            print(f"ROOM NAME: {self.current_room.name}\n")
            print(f"ROOM DESCRIPTION: {self.current_room.description}\n")
        else: 
            print('invalid movement')
        
        return True

    def addItem(self, itemName):
        self.items.append(Item(itemName,"sample description"))

    def getItem(self,name):

        for item in self.current_room.items:
            if name in item.name:
                self.current_room.items.remove(item)
                # add the item to player inventory
                self.items.append(item)
                item.on_take(name)
                return True

        print(f'\n{color.RED} {name} is not in  {self.current_room.name} room {color.END}')
        return False

    def dropItem(self,name):
        for item in self.items:
            if name in item.name:
                # remove the item from player inventory
                self.items.append(item)
                # add item to room
                self.current_room.addItem(item)
                item.on_drop(name)
                return True
        print(f'\n{color.RED}  {name} is not in the inventory {color.END}')
        return False

    def getItems(self):
        if len(self.items) > 0:
            print('\nThese are the inventory:')
            count = 1
            for item in self.items:
                print(f'\nItem {count}: {item.name}')
                count += 1
        else: print('Inventory is empty!')

    def printItemsInView(self):
        if len(self.current_room.items) > 0:
            print(f'\nThese are items in the {self.current_room.name} room:\n')

            count = 1
            itemsStr = ""
            for item in self.current_room.items:
                itemsStr += f'[{count}]: {item.name}    '
                count += 1
            print(itemsStr)
        else: print('Room is empty!')


           # print(color.BOLD + 'Hello World !' + color.END) 
        





