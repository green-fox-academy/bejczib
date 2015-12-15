from menu import *

# def print_a():
#     return('alma')

# def print_b():
#     return('korte')

# def print_c():
#     return('barack')

def new_game_action():
    print(input('Name: '))
    choose = 0
    while choose != 3:
        new_game_items = [
                            MenuItems(1, 'Renter Name', new_game_action),
                            MenuItems(2, 'Continue', None),
                            MenuItems(3, 'Quit', exit)
                         ]
        new_game_menu = Menu(new_game_items)
        new_game_menu.print_menu()
        choose = int(input('Choose: '))
        new_game_menu.select_menu(choose)






