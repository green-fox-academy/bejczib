reverse_text = open("reversed_zen_order.txt")
text = reverse_text.read()
lines = text.split('\n')

def reverse(text):
    return '\n'.join(lines[::-1])
    
print(reverse(text))
