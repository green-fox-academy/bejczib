reverse_text = open("encoded_zen_lines.txt")
text = reverse_text.read()

def alma(text):
    new = ''
    for i in text:
        if i == ' ':
            new += i
        elif i == '\n':
            new += i
        else:
            new += chr(ord(i)-1)
    return new

print(alma(text))
