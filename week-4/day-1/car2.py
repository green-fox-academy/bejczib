class Car(object):
    def __init__(self, color, type, km):
        self.color = color
        self.type = type
        self.km = km

    def ride(self, km):
        self.km += km

tesla = Car('pink', 'Tesla S', 1200)
lada = Car('red', 'Lada 1200', 40000)

tesla.ride(220)

print(tesla.km)
print(lada.type)
