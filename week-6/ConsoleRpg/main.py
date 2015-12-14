from menu import *

menu.print_menu()
choose = input('Choose an item: ')
while choose != '3':
    menu.select_menu(choose)
    while choose == '1':
        new.display_name(input('enter your name: '))
        new.print_menu()
        choose2 = input('choose an item: ')
        while choose2 == '1':
            new.display_name(input('enter your name: '))
            new.print_menu()
            choose2 = input('choose an item: ')
        if choose2 == '2':
            print('Hang on bro, not finished yet.')

        if choose2 =='3':
            quit.print_menu()j
    choose = input('Choose an item: ')
