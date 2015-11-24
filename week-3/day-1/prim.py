temp = input('adj meg egy szamot\n')
num = int(temp)

has_divisor = 0
i = 2
while i < num and not has_divisor:
    if num % i == 0:
        has_divisor = 1
    i += 1

if has_divisor or num == 0 or num == 1:
    print('The number is not prime')
else:
    print('The number is a prime')
