from color import color

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def on_take(self, name):
                # print(f'\n{color.RED}  {name} is not in the inventory {color.END}')

        print(f'\n{color.GREEN} {name} has been picked up succesfully! {color.END}')

    def on_drop(self, name):
        print(f'\n{color.GREEN} {name} has been dropped succesfully!\n{color.END}')