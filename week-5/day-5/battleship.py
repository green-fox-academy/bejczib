class Arena:
    def __init__(self, grid):
        self.grid = grid


    def is_hit(self, x, y):
        return self.grid[x][y] == 1

    def swap(self, x, y):
        if self.is_hit(x,y):
            self.grid[x][y] = 5
        return self.grid[x][y]




