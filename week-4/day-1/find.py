student = [
    {'name': 'Tibi', 'age': 8},
    {'name': 'Adorjan', 'age': 9},
    {'name': 'Agoston', 'age': 6},
    {'name': 'Aurel', 'age': 7},
    {'name': 'Dezso', 'age': 12}
]

student_name_at_least_8= []

# def age_8():
#     student_name_at_least_8= []
#     for value in student:
#         if value['age'] <= 8:
#             student_name_at_least_8.append(value['name'])
#     return student_name_at_least_8
# print(age_8())

def letter_a():
    student_age_letter_a = []
    for value in student:
        if value['name'][0] == ('A'):
            student_age_letter_a.append(value['age'])
    return student_age_letter_a

print(letter_a())
