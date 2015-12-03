filename = open("todo_list.txt", "r+")
string = filename.read()

def add_item(string):
    new_item= input('the new todo is: ')
    return new_item


filename.write("\n" + add_item(string))
filename.close()
