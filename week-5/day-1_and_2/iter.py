class Fibonacchi:
    def __init__(self, count):
        self.count = count
        self.a = 0
        self.b = 1
        self.i = 0

    def __next__(self):
        if self.i >=self.count:
            raise StopIteration()

        self.i += 1
        self.a, self.b = self.a + self.b, self.a
        return self.b

    def __iter__(self):
        return self

for n in Fibonacchi(5):
    print(n)
print('*' * 30)

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        return iter(self.items)

class Sword:
    pass

class Coins:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Coin: {}'.format(self.value)

inventory = Inventory()
inventory.add(Coins(5))
inventory.add(Coins(1))
inventory.add(Coins(2))

for n in inventory:
    print(n)
