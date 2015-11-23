import sys

temp = input('Adj meg egy szamot 1-99ig!\n')
user_input = int(temp)
if user_input >=99:
    sys.stdout.write('1-99!')
elif user_input < 1:
    sys.stdout.write('1-99!')
else:
    if user_input >= 90:
        sys.stdout.write('XC')
        user_input = user_input-90
    if user_input >= 50:
        sys.stdout.write('L')
        user_input = user_input-50
    if user_input >= 40:
        sys.stdout.write('XL')
        user_input = user_input-40
    while user_input >= 10:
        sys.stdout.write('X')
        user_input = user_input-10
    if user_input >= 9:
        sys.stdout.write('IX')
        user_input = user_input-9
    if user_input >= 5:
        sys.stdout.write('V')
        user_input = user_input-5
    if user_input >= 4:
        sys.stdout.write('IV')
        user_input = user_input-4
    while user_input >= 1:
        sys.stdout.write('I')
        user_input = user_input-1
