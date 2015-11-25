class MySuperString(object):
    def __init__(self, my_string):
        self.my_string = my_string

    def reverse(self):
        rev_string = ''
        index = len(self.my_string)-1

        for i in range(index, -1, -1):
            rev_string += self.my_string[i]
            
        print(rev_string)

        #second solution:

        # while index >= 0:
        #     rev_string += self.my_string[index]
        #     index -= 1
        # print(rev_string)
