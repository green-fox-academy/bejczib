class MyAverage(object):
    def __init__(self, my_list):
        self.my_list = my_list

    def average(self):
        summ = 0
        for i in self.my_list:
            summ += i
        summ /= len(self.my_list)
        return summ
