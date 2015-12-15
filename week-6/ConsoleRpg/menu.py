import commands

def main_menu():
    items = [
                 MenuItems(1, 'New Game', display_name),
                 MenuItems(2, 'load', None),
                 MenuItems(3, 'Quit', None)
                 ]
    return Menu(items)

class Menu:
    def __init__(self, items):
        self.items = items

    def print_menu(self):
        for item in self.items:
            print('{}: {}'.format(item.option, item.name))

    def select_menu(self, choose):
        for item in self.items:
            if item.option == choose:
                return item.cmd()

class MenuItems:
    def __init__(self, option, name, cmd):
        self.option = option
        self.name = name
        self.cmd = cmd

