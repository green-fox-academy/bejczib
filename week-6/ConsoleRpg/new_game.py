def new_game_menu():
    items = [
                 MenuItems(1, 'Reenter name', display_name),
                 MenuItems(2, 'Continue', load_game),
                 MenuItems(3, 'Quit', quit_game)
                 ]
    return Menu(items)

class NewGame(MenuItems):
    def display_name(self, name):
        print(name)

