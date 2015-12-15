from main_menu import *
from commands import *


menu = main_menu()
menu.print_menu()
choose = int(input('Choose an item: '))
menu.select_menu(choose)

