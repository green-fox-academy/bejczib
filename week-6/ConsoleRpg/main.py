from main_menu import *
from commands import *
from menu import *

menu = main_menu()
menu.print_menu()
menu.select_menu(int(input('Choose: ')))

