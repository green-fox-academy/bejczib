from random import randint

guessed_number = random.randint(0, 10)
number_of_guesses = 6

def get_integer():
    num = int(input('Enter an integer: '))
    return num

while number_of_guesses > 0:
    try:
        guess= get_integer()
    except ValueError:
        print('You entered a wrong value')
    else:
        if guess == guessed_number:
            print('you got it!')
            break
        elif guess < guessed_number:
            print('Think bigger!')
            number_of_guesses -=1
        else:
            print('Think smaller!')
            number_of_guesses -=1
if number_of_guesses == 0:
    print('You are such a lame, the number was %d' % guessed_number)
