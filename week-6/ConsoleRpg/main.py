from menu import *

def main():
    menu = main_menu()
    while True:
        menu.print_menu()
        choose = int(input('Choose an item: '))
        menu.select_menu(choose)

main()
