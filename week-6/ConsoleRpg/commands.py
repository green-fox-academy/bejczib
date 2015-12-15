from menu import *

# def print_a():
#     return('alma')

# def print_b():
#     return('korte')

# def print_c():
#     return('barack')

def new_game_action():
    print(input('Name: '))
    new_game_items = [
                        MenuItems(1, 'Renter Name', None),
                        MenuItems(2, 'Continue', None),
                        MenuItems(3, 'Quit', None)
                     ]
    new_game_menu = Menu(new_game_items)
    new_game_menu.print_menu()



