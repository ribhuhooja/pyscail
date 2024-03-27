from dataclasses import dataclass
import random

import pyscail as scail
from settings import Constants


@dataclass
class Cell:
    i: int
    j: int
    alive: bool

    def next(self):
        neighbors = scail.cells(
            scail.kernels.wrap_moore_neighborhood(
                self.i,
                self.j,
                Constants.GAME_WIDTH,
                Constants.GAME_HEIGHT,
            )
        )

        num_alive = 0
        for cell in neighbors:
            if cell.alive:
                num_alive += 1

        if num_alive < 2 or num_alive > 4:
            return Cell(self.i, self.j, False)
        elif num_alive == 3:
            return Cell(self.i, self.j, True)
        else:
            return Cell(self.i, self.j, self.alive)

    def display(self):
        color_val = 255 if self.alive else 0
        return (color_val, color_val, color_val)


def initialize(i, j, width, height):
    alive = True if random.random() > 0.05 else False
    return Cell(i, j, alive)


def lerp(a, b, t):
    return a + (b - a) * t


if __name__ == "__main__":
    scail.run(initialize, lambda: None, mutate=False)
