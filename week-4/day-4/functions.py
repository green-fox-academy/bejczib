class Functions(object):
    def __init__(self, path):
        self.path = path

    def file_read(self):
        with open(self.path) as todo_list:
            return [line.rstrip() for line in todo_list.readlines()]

    def save(self, todos):
        with open(self.path, 'w') as todo_list:
            todo_list.write('\n'.join(todos))

    def add_item(self, todo):
        todos = self.file_read()
        todos.append(todo)
        self.save(todos)

    def print_items(self):
        items = self.file_read()
        for i in range(len(items)):
            print('{}: {}'.format(i+1, items[i]))

    def remove(self, remove):
        todos = self.file_read()
        deleted = remove
        removed_item = todos.pop(deleted-1)
        self.save(todos)
        return removed_item

    def remove_all(self):
        todos = self.file_read()
        del todos[:]
        self.save(todos)
