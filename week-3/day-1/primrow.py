def isprim(num):
    has_divisor = 0
    i = 2
    while i < num and num != has_divisor:
        if num % i == 0:
            has_divisor = 1
        i += 1
    if has_divisor or num == 0 or num == 1:
        return False
    else:
        return True

n = 0
while n < 100:
    if isprim(n):
        print(n)
    n += 1
