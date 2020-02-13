class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def on_take(self, name):
        print(f'Item {name} has been picked up')

    def on_drop(self, name):
        print(f'Item {name} has been dropped!')