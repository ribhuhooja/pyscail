from dataclasses import dataclass
from typing import Tuple
import random


@dataclass
class Cell:
    is_alive: bool


class Grid:
    cells: list[list[Cell]]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [
            [Cell(random.choice([True, False])) for j in range(self.height)]
            for i in range(self.width)
        ]

    def step_grid(self):
        new_cells = [
            [Cell(self.cells[i][j].is_alive) for j in range(self.height)]
            for i in range(self.width)
        ]
        for i in range(self.width):
            for j in range(self.height):
                cell = self.cells[i][j]
                neighbors = [
                    self.cells[x][y]
                    for (x, y) in _neighboringIndicesWrap(i, j, self.width, self.height)
                ]
                num_alive_neighbors = len(list(filter(lambda x: x.is_alive, neighbors)))
                if cell.is_alive:
                    if num_alive_neighbors < 2 or num_alive_neighbors > 3:
                        new_cells[i][j].is_alive = False
                else:
                    if num_alive_neighbors == 3:
                        new_cells[i][j].is_alive = True

        self.cells = new_cells


def _neighboringIndices(
    x: int, y: int, width: int, height: int
) -> list[Tuple[int, int]]:
    neighbors = []
    for i in range(max(x - 1, 0), min(x + 2, width)):
        for j in range(max(y - 1, 0), min(y + 2, height)):
            neighbors.append((i, j))
    neighbors.remove((x, y))
    return neighbors


# Wraps from the right edge to left and top edge to the bottom
# Like a video game in which if you go off the edge you come back
# on the other side
def _neighboringIndicesWrap(
    x: int, y: int, width: int, height: int
) -> list[Tuple[int, int]]:
    neighbors = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i % width, j % height) != (x % width, y % height):
                neighbors.append((i % width, j % height))
    return neighbors
