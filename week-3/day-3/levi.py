class MyUpper(object):
    def __init__(self, my_string):
        self.my_string = my_string


    def second_upper(self):
        changed = ''
        self.my_string = self.my_string.lower()
        for i in range(len(self.my_string)):
            if i % 2 == 0:
                changed += self.my_string[i].upper()
            else:
                changed += self.my_string[i]
        return changed
