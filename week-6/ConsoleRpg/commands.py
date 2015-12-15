from menu import *
from character import *

player = Character()

def new_game_action():
    player.name = input('Name: ')
    print(player.name)
    choose = 0
    new_game_items = [
                        MenuItems(1, 'Renter Name', new_game_action),
                        MenuItems(2, 'Continue', game_continue),
                        MenuItems(3, 'Quit', exit_game)
                     ]
    new_game_menu = Menu(new_game_items)
    new_game_menu.make_new_menu()

def exit_game():
    exit_game_items = [
                      MenuItems(1, 'Save and Quit', exit),
                      MenuItems(2, 'Quit without Save', exit),
                      MenuItems(3, 'Resume', None)
                     ]
    exit_game_menu = Menu(exit_game_items)
    exit_game_menu.make_new_menu()

def game_continue():
    player.roll_health()
    player.roll_luck()
    player.roll_dexterity()
    print('{}: {},{},{}'.format(player.name, player.health, player.dexterity, player.luck))








