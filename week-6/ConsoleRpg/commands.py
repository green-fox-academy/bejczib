from menu import *
from character import *

player = Character()

def new_game_action():
    player.name = input('Name: ')
    print(player.name)
    choose = 0
    new_game_items = [
                        MenuItems(1, 'Renter Name', new_game_action),
                        MenuItems(2, 'Continue', roll_stat),
                        MenuItems(3, 'Quit', exit_game)
                     ]
    new_game_menu = Menu(new_game_items)
    new_game_menu.print_menu()
    new_game_menu.select_menu(int(input('Choose: ')))

def exit_game():
    exit_game_items = [
                      MenuItems(1, 'Save and Quit', exit),
                      MenuItems(2, 'Quit without Save', exit),
                      MenuItems(3, 'Resume', None)
                     ]
    exit_game_menu = Menu(exit_game_items)
    exit_game_menu.print_menu()
    exit_game_menu.select_menu(int(input('Choose: ')))

def roll_stat():
    player.roll_health()
    player.roll_luck()
    player.roll_dexterity()
    print('{}: {} | {} | {}'.format(player.name, player.health, player.dexterity, player.luck))
    roll_game_items = [
                        MenuItems(1, 'Reroll', roll_stat),
                        MenuItems(2, 'Continue', select_potion),
                        MenuItems(3, 'Quit', exit_game)
                     ]
    roll_stat_menu = Menu(roll_game_items)
    roll_stat_menu.print_menu()
    roll_stat_menu.select_menu(int(input('Choose: ')))

def select_potion():
    select_potion_items = [
                      MenuItems(1, 'Potion of Health', selected_potion),
                      MenuItems(2, 'Potion of Dexterity', selected_potion),
                      MenuItems(3, 'Potion of Luck', selected_potion)
                     ]
    print('<--Select Potion-->')
    select_potion_menu = Menu(select_potion_items)
    select_potion_menu.print_menu()
    choice = int(input('Choose: '))
    player.get_inventory(select_potion_items[choice-1].name)
    select_potion_menu.select_menu(choice)


def selected_potion():
    selected_potion_items = [
                      MenuItems(1, 'Reselect Potion', select_potion),
                      MenuItems(2, 'Continue', display_player),
                      MenuItems(3, 'Quit', exit_game)
                     ]
    selected_potion_menu = Menu(selected_potion_items)
    selected_potion_menu.print_menu()
    selected_potion_menu.select_menu(int(input('Choose: ')))

def display_player():
    print('{}: {} | {} | {} | {}'.format(player.name, player.health, player.dexterity, player.luck, player.inventory))
    display_player_items = [
                      MenuItems(1, 'Begin', None),
                      MenuItems(2, 'Save', None),
                      MenuItems(3, 'Quit', exit_game)
                     ]
    display_player_menu = Menu(display_player_items)
    display_player_menu.print_menu()
    display_player_menu.select_menu(int(input('Choose: ')))










