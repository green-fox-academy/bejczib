class Count(object):
    def __init__(self, my_string):
        self.my_string = my_string

    def count(self):
        char_count = 0
        for i in self.my_string:
            char_count += 1
        print(char_count)
