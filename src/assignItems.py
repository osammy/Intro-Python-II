import random

def randomAssign(Item):

    items = [
        {
            'name':'water',
            'description':'A water'
        },
        {
            'name':'bible',
            'description':'A bible'
        },
        {
            'name':'box',
            'description':'A box'
        },
        {
            'name':'watch',
            'description':'A watch'
        },
        {
            'name':'coin',
            'description':'A coin'
        },
        {
            'name':'clue',
            'description':'A clue'
        },
        {
            'name':'gun',
            'description':'A gun'
        },
        {
            'name':'pen',
            'description':'A pen'
        },
        {
            'name':'rope',
            'description':'A rope'
        },
    ]

    itemLength = len(items)
    # get a random integer, that will represent the number of items to be inserted
    randNum = random.randint(1, 4)
    # get a list of unique integer index, to use to select items index
    randIndexes = random.sample(range(itemLength), randNum)

    # return items randomly selected
    return [ Item(items[index]['name'],items[index]['description'])  for index in randIndexes ]

