from dataclasses import dataclass
import random

import pyscail as scail
from settings import Constants

ORIGINAL_POPULATION_DENSITY = 0.5


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

        if num_alive < 2 or num_alive > 3:
            alive_in_next_gen = False
        elif num_alive == 3:
            alive_in_next_gen = True
        else:
            alive_in_next_gen = self.alive

        return Cell(self.i, self.j, alive_in_next_gen)

    def display(self):
        color_val = 255 if self.alive else 0
        return (color_val, color_val, color_val)


def initialize(i, j, width, height):
    init_list = [(100, 100), (100, 101), (100, 99), (99, 100), (101, 99)]
    # alive = True if random.random() < ORIGINAL_POPULATION_DENSITY else False
    alive = True if (i, j) in init_list else False
    return Cell(i, j, alive)


def lerp(a, b, t):
    return a + (b - a) * t


if __name__ == "__main__":
    scail.run(initialize, lambda: None, mutate=False)
