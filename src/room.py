# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item
from assignItems import randomAssign

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = randomAssign(Item)
        self.n_to =  None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def addItem(self, item):
        self.items.append(item)

    def __str__(self):
        return f'{self.name}: {self.description}'
