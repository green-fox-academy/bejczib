# af = 123
#
# def double(szam):
#     szam *= 2
#
# ag = 'kuty'
# def plus(string):
#     string += 'a'
#     return string
#
# print(plus(ag))
#
# ag2 = ['rep', 'alm', 'kacs', 'ann']
#
# def plus_a(text):
#     for i in range(len(text)):
#         text[i] = plus(ag2[i])
#
#     return text
#
# print(plus_a(ag2))

numbers = [1,2,3,4,5]
def sum_num(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(sum_num(numbers))
