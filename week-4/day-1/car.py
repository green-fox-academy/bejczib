# lada = {
#     'color': 'red',
#     'type': 'Lada 1200'
#     'km': 40000
# }

# tesla = {
#     'color': 'pink',
#     'type': 'Tesla S',
#     'km': 1200
# }

def init_car(color, type, km):
    car = {'color': '', 'type': '', 'km': 0}
    car['color'] = color
    car['type'] = type
    car['km'] = km
    return car

lada = init_car('red', 'Lada 1200', 40000)
print(lada)

def ride(car, km):
    car['km'] += km
