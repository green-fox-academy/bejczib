import random

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

numbers = [1,2,3,4,5,6,7,8,9]
def sudoku_solver(puzzle):
    pass

def pretty_print(puzzle):
    for row in puzzle:
        for element in row:
            print(str(element) + ' ', end = '')
        print()

def search_swap(puzzle):
    for row in puzzle:
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = random.choice(numbers)
    return puzzle

pretty_print(puzzle)
print('*' * 20)
pretty_print(search_swap(puzzle))

def search_num(puzzle):
    for row in puzzle:
        for i in range(len(row))
            if row[i] ==
