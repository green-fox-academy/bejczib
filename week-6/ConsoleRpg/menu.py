class Menu:
    def __init__(self, items):
        self.items = items

    def print_menu(self):
        for item in self.items:
            print('{}: {}'.format(item.option, item.name))

    def select_menu(self, choose):
        for item in self.items:
            if item.is_valid_choose(choose):
                return item.call_cmd()
        print('Incorrect input!')


class MenuItems:
    def __init__(self, option, name, cmd):
        self.option = option
        self.name = name
        self.cmd = cmd

    # def __repr__(self):
    #      return

    def is_valid_choose(self, choose):
        return choose == self.option

    def call_cmd(self):
        return self.cmd()

