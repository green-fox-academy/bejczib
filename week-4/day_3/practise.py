students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]


# def candie_4():
#     db = 0
#     for value in students:
#         if value['candies'] > 4:
#             db += 1
#     return db
#
# print(candie_4())

result = len(list(filter(lambda x: x['candies'] > 4, students)))

print(result)
