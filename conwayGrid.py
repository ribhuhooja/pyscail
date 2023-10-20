"""Provides Grid, a class that holds all the cells in the game of life"""

from dataclasses import dataclass
from typing import Tuple
import random


@dataclass
class Cell:
    is_alive: bool


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells: list[list[Cell]] = [
            [Cell(False) for j in range(self.height)] for i in range(self.width)
        ]

    def step_grid(self):
        """From the current generation of cells, produce the next one

        For each alive cell in the grid, if it has 2 or 3 alive neighbors it remains alive.
        Otherwise, it dies.
        For each dead cell, if it has exactly 3 alive neighbors, it becomes alive. Otherwise, it remains dead.
        """
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

    def clear(self):
        """Kills all the cells"""
        for row in self.cells:
            for cell in row:
                cell.is_alive = False

    def randomize(self):
        """Randomly sets each cell to either alive or dead"""
        self.cells = [
            [Cell(random.choice([True, False])) for j in range(self.height)]
            for i in range(self.width)
        ]


def _neighboringIndicesWrap(
    x: int, y: int, width: int, height: int
) -> list[Tuple[int, int]]:
    """Returns the indices of neighboring cells given the index of some cell

    Wraps from the right edge to left and top edge to the bottom
    like a video game in which if you go off the edge you come back
    on the other side
    """
    neighbors = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i % width, j % height) != (x % width, y % height):
                neighbors.append((i % width, j % height))
    return neighbors
