array = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def snail(array):
    output = []
    temp = []
    for num in array[0]:
        output.append(num)
    for i in range(len(array)):
        for num in array[i]:
            temp.append(num)
    print(temp)

snail(array)
