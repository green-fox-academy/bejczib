reverse_text = open("reversed_zen_lines.txt")
text = reverse_text.read()
lines = text.split('\n')

def reverse(text):
    reversed_lines = []
    for line in lines:
        reversed_line = line[::-1]
        reversed_lines.append(reversed_line)

    return '\n'.join(reversed_lines)



print(reverse(text))
