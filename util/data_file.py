import os
class DataFile():

    def __init__(self, filename):

        self.grid = []
        self.grid_rows = 0
        self.grid_cols = 0
        if os.path.exists(filename):

            with open(filename, mode="r") as f:
                self.lines = [line.rstrip() for line in f]

        else:
            print("File does not exists")
            exit(1)

    def convert_to_grid(self):

        for line in self.lines:
            self.grid.append(list(line))

        self.grid_rows = len(self.grid)
        self.grid_cols = len(self.grid[0])