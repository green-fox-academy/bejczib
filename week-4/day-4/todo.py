from functions import *
import os

def clr():
    os.system('clr' if os.name=='nt' else 'clear')

def main():
    todo = Functions("todo_list.txt")
    doing = Functions("doing_list.txt")
    done = Functions("done_list.txt")
    clr()
    menu(todo, doing, done)

def menu(todo, doing, done):
    print('\n' '\t','*'*80, '\n' '\t' ,'*'*22,' Balint Bejczi - ToDo Application ','*'*22, '\n' '\t','*'*80)
    print('\n')
    print("                    * * *                                             * * *")
    print("                    *                           MENU                      *")
    print("                    *                                                     *")
    print("                            1. Add new                                     ")
    print("                            2. TODOs to wait                               ")
    print("                            3. Mark done                                   ")
    print("                            4. Delete                                      ")
    print("                            5. Mark doing                                  ")
    print("                    *       6. Delete all                                 *")
    print("                    *       E(x)it                                        *")
    print("                    * * *                                             * * *")
    print('\n' *2)
    choose = input("Choose which functions you'd like to use: ")
    while choose != 'x':
        clr()
        print("                    * * *                                             * * *")
        print("                    *                           MENU                      *")
        print("                    *                                                     *")
        print("                            1. Add new                                     ")
        print("                            2. TODOs to wait                               ")
        print("                            3. Mark done                                   ")
        print("                            4. Delete                                      ")
        print("                            5. Mark doing                                  ")
        print("                    *       6. Delete all                                 *")
        print("                    *       E(x)it                                        *")
        print("                    * * *                                             * * *")
        print('\n')
        print('Your current tasks are the following:')
        doing.print_items()

    # ADD NEW TODO ------------------------------------------------------ #

        if choose == '1':
            todo.add_item(input('add a new item: '))
            print('\n')
            print('Your TODO is saved!')
            choose5 = input('do you want to add more? (Y)es or (N)o :')
            while choose5 == 'y':
                todo.add_item(input('add a new item: '))
                choose5 = input('do you want to add more? (Y)es or (N)o :')

    # PRINT THE LIST OF THE WAITING TODOS -------------------------------- #

        elif choose == '2':
            print('\n'*2)
            print('This are your TODOs to wait:')
            todo.print_items()

    # MARK AN ITEM DONE ID ITS DONE --------------------------------- #

        elif choose == '3':
            print('\n'*2)
            removed_item = doing.remove(int(input('which one is done: ')))
            print('\n')
            print('Lay down, you have one less task')
            done.add_item(removed_item)
            print('\n')
            choose2 = input('Enter your done list? (Y)es or (N)o: ')
            if choose2 == 'y':
                print('\n')
                print('These are the tasks you did:')
                done.print_items()
            elif choose2 == 'n':
                pass

    # DELETE ITEM FROM TODO OR DONE LIST ---------------------------- #

        elif choose == '4':
            print('\n')
            choose3 = input('From (D)oing or (T)oDo? : ')
            if choose3 == 'd':
                print('\n')
                doing.remove(int(input('From above which one do you want to delete: ')))
                print('Your item was deleted!')
            elif choose3 == 't':
                print('\n'*2)
                print('Your TODOs to wait:')
                todo.print_items()
                todo.remove(int(input('which one do you want to delete: ')))
                print('Your item was deleted')

    # MARK AN ELEMENT DOING ------------------------------------------ #

        elif choose == '5':
            print('\n'*3)
            todo.print_items()
            removed_item = todo.remove(int(input('which one would you like to do: ')))
            doing.add_item(removed_item)
            print('\n')
            print('Your doing list will by updated in a minute: ')
            doing.print_items()

    # DELETE ALL ITEM IN TODO OR DONE LIST --------------------------- #

        elif choose == '6':
            print('\n')
            choose4 = input('refresh (T)oDo or (D)one. : ')
            if choose4 == 't':
                todo.remove_all()
                print('\n')
                print('Your todo list is empty now')
            elif choose4 == 'd':
                done.remove_all()
                print('\n')
                print('Your done list is empty now')

        else:
            print('\n'*2)
            print("I don't understand")
            print("Please choose from number above!")

        print('\n')
        choose = input("Do you want to use an other function? Your choice: ")

main()
