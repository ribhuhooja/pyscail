from typing import Any, List


class Grid:
    def __init__(self, width, height, initialize, mutate=True):
        self.width = width
        self.height = height
        self.initialize = initialize
        self.cells: List[List[Any]] = self.initial_cells()
        self.mutate = mutate

    def step_grid(self):
        if self.mutate:
            for i in range(self.width):
                for j in range(self.height):
                    self.cells[i][j].next()
        else:
            new_cells = [[None for _ in range(self.height)] for _ in range(self.width)]
            for i in range(self.width):
                for j in range(self.height):
                    new_cells[i][j] = self.cells[i][j].next()

            self.cells = new_cells

    def reset(self):
        self.cells = self.initial_cells()

    def initial_cells(self):
        cells = [
            [self.initialize(i, j, self.width, self.height) for j in range(self.height)]
            for i in range(self.width)
        ]

        return cells
