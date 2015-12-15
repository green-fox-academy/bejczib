class Menu:
    def __init__(self, items):
        self.items = items

    def print_menu(self):
        for item in self.items:
            print('{}: {}'.format(item.option, item.name))

    def select_menu(self, choose):
        for item in self.items:
            if item.option == choose:
                return item.cmd()

    def make_new_menu(self):
        self.print_menu()
        self.select_menu(self.validate_user_input())

    def validate_user_input(self):
        while True:
            try:
                user_input = int(input('Choose: '))
                break
            except ValueError:
                print('Faszfej vagy')

        return user_input


class MenuItems:
    def __init__(self, option, name, cmd):
        self.option = option
        self.name = name
        self.cmd = cmd

