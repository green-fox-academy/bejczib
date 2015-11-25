class WhiteSpace:
    def __init__(self, my_string):
        self.my_string = my_string

    def change(self):
        changed = ''
        for i in self.my_string:
            if i == ' ':
                changed += '_'
            else:
                changed += i
        return changed
