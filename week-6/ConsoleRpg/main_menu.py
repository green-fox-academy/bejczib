from menu import *
from commands import *

def main_menu():
    items = [
                 MenuItems(1, 'New Game', new_game_action),
                 MenuItems(2, 'load', load_menu),
                 MenuItems(3, 'Quit', exit_game)
                 ]
    return Menu(items)


