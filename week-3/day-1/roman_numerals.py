# n =2008
# result = ''
# if n >= 1000:
#     result +=('M')
#     n = n-1000
# elif n >= 500:
#     result +=('D')
#     n = n-500
# elif n >= 100:
#     result +=('C')
#     n = n-100
# elif n >= 90:
#     result +=('XC')
#     n = n-90
# elif n >= 50:
#     result += ('L')
#     n = n-50
# elif n >= 40:
#     result += ('XL')
#     n = n-40
# while n >= 10:
#     result += ('X')
#     n = n-10
# if n >= 9:
#     result += ('IX')
#     n = n-9
# elif n >= 5:
#     result += ('V')
#     n = n-5
# elif n >= 4:
#     result += ('IV')
#     n = n-4
# while n >= 1:
#     result += ('I')
#     n = n-1
#
# print(result)



def soultion(string):
    values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    return sum(map(lambda x: values[x], string))

print(solution('IV'))
