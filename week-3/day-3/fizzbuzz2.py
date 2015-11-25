def is_fizzish(number, base):
    if number % base == 0 or str(base) in str(number):
        return True
    else:
        return False

def fizz_buzz(min, max):
    n = min
    while n < max:
        if is_fizzish(n, 3) and is_fizzish(n, 5):
            print("fizzbuzz")
        elif is_fizzish(n, 3):
            print("fizz")
        elif is_fizzish(n, 5):
            print("buzz")
        else:
            print(n)
        n += 1


fizz_buzz(1,50)
