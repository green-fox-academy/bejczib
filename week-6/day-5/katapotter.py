
def discounter(array):
    price = 0
    while array != []:
        unique = list(set(array))
        price += amount(unique)
        array = [i for i in array if i not in unique or unique.remove(i)]

        # array2 = []
        # for item in array:
        #     if item in unique:
        #         unique.remove(item)
        #     else:
        #         array2.append(item)
        # array = array2
    return price

def amount(unique_list):
    discounts = [1, 0.95, 0.9, 0.8, 0.75]
    books = len(unique_list)
    discount = discounts[books - 1]
    return books * discount * 8







