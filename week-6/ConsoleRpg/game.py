from menu import *
from character import *

class Game:
    def __init__(self):
        self.menu = self.main_menu()
        self.player = Character()

    def main_menu(self):
        return Menu([
                 MenuItems(1, 'New Game', self.new_game_menu),
                 MenuItems(2, 'load', self.not_implemented),
                 MenuItems(3, 'Quit', exit)
                 ])

    def not_implemented(self):
        return 'not implemented'

    def new_game_menu(self):
       self.menu = Menu([
                        MenuItems(1, 'Renter Name', self.not_implemented),
                        MenuItems(2, 'Continue', self.not_implemented),
                        MenuItems(3, 'Quit', exit)
                     ])

def main():
    game = Game()
    while True:
        menu = game.menu
        menu.print_menu()
        choose = menu.ask_user()
        result = menu.select_menu(int(choose))
        player.name = menu.ask_user()
        print(result)
main()


