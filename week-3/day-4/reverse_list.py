list = [1,2,3,4,5,6,7,8]

def reverse_list():
    rev_list = []
    index = len(list)-1

    for i in range(index, -1, -1):
        rev_list.append(list[i])

    return rev_list

print(reverse_list())
