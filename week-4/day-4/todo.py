def menu():
    print('\n','*'*80, '\n','*'*30,' Lab.foox Inc. -- ToDo Application ','*'*30, '\n','*'*80)
    print('\n')
    print('1. add an item\n')
    print('2. delete item\n')
    print('3. complete item\n')
    print('(E)xit\n')
    choose = input("Choose which functions you'd like to use: ")
    while choose != 'e':
        if choose == '1':
            print('hali')
        elif choose == '2':
            print('hali')
        elif choose == '3':
            print('hej')
        else:
            print("WRONG OPTION. SORRY, TRY AGAIN!")
        choose = input("Choose which functions you'd like to use: ")

menu()
