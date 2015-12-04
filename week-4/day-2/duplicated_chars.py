reverse_text = open("duplicated_chars.txt")
text = reverse_text.readlines()

remove = ''
def remove_duplicate(text):
    alma = ''
    for line in text:
        remove = line[::2]
        alma +=remove
    return alma
print(remove_duplicate(text))
