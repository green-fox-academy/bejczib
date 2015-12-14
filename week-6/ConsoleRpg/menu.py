class Menu:
    def __init__(self):
        pass

    def get_menu(self):
        return  {'1': 'New Game',
                 '2': 'Load Game',
                 '3': 'Exit'
                }

    def print_menu(self):
        menu = self.get_menu()
        for i in range(len(menu)):
            print('{}: {}'.format(i+1, menu[str(i+1)]))

    def select_menu(self, choose):
        if '1' <= choose <='3':
            return choose
        else:
            return 'Incorrect answer!'


class NewGame(Menu):

    def display_name(self, name):
            print(name)

    def get_menu(self):
            return  {'1': 'Reenter Name',
                     '2': 'Continue',
                     '3': 'Quit'
                    }
    def print_menu(self):
        menu = self.get_menu()
        for i in range(len(menu)):
            print('{}: {}'.format(i+1, menu[str(i+1)]))

class LoadGame:
    pass

class QuitGame:
    def get_menu(self):
            return  {'1': 'Quit and save',
                     '2': 'Quit without saving',
                     '3': 'Resume'
                    }

    def print_menu(self):
        menu = self.get_menu()
        for i in range(len(menu)):
            print('{}: {}'.format(i+1, menu[str(i+1)]))



menu = Menu()
new = NewGame()
quit = QuitGame()

# menu.print_menu()
# menu.select_menu()
