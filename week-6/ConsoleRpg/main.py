from main_menu import *
from commands import *
from menu import *

menu = main_menu()
menu.print_menu()
choose = menu.validate_user_input()
menu.select_menu(choose)

