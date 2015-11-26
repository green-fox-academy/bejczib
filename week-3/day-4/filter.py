numbers = [1,2,3,4,5,6,7,8]

output = []

def even_pull():
    for i in numbers:
        if i % 2 ==0:
            output.append(i)
    return output

print(even_pull())
