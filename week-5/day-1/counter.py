def count_letters(string):
    output = {}
    for letter in string:
        output[letter] = string.count(letter)
    return output
