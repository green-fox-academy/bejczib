

def is_palindrome(word):
    return word == word[::-1]

def search_palindrome(my_string):
    words= my_string.split()
    result = []
    for word in words:
        for i in range(0, len(word)-1):
            for j in range(i+1, len(word)):
                fregment = word[i:j+1]
                if is_palindrome(fregment):
                    result.append(fregment)
    return result

print(search_palindrome('dog goat dad duck doodle never'))
