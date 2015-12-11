
class MyMagic:
    def __init__(self, names):
        self.names = names

    def array_of_names(self):
        return list(map(lambda u: u['name'], self.names))

    def names_with_j(self):
        return list(filter(lambda x: x[0] == 'J', self.array_of_names()))
