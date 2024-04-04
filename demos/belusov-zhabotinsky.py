from dataclasses import dataclass
from math import floor
import random

import pyscail as scail


class Constants:
    SIMULATION_WIDTH = 400
    SIMULATION_HEIGHT = 300
    CELL_SIZE = 1
    INITIAL_FPS = 8

    K1 = 2
    K2 = 3
    NUM_STATES = 200
    G = 70
    NUM_COLORS = 8
    COLORS = [(255 - i, 128 - i // 2, i) for i in range(0, 256, int(256 / NUM_COLORS))]


print(Constants.COLORS)


settings = (
    scail.Settings.default()
    .set_dimensions(
        Constants.SIMULATION_WIDTH, Constants.SIMULATION_HEIGHT, Constants.CELL_SIZE
    )
    .set_initial_fps(Constants.INITIAL_FPS)
)


@dataclass
class Cell:
    i: int
    j: int
    state: int

    def next(self):
        neighbors = scail.cells(
            scail.kernels.wrap_moore_neighborhood(
                self.i,
                self.j,
                Constants.SIMULATION_WIDTH,
                Constants.SIMULATION_HEIGHT,
            )
        )

        if self.state == Constants.NUM_STATES - 1:
            next_state = 0
        else:
            ill = 0
            infected = 0
            for neighbor in neighbors:
                if neighbor.state == Constants.NUM_STATES - 1:
                    ill += 1
                elif neighbor.state != 0:
                    infected += 1

            if self.state == 0:
                next_state = floor(infected / Constants.K1) + floor(ill / Constants.K2)
            else:
                s = self.state + sum([neighbor.state for neighbor in neighbors])
                next_state = floor(s / (1 + infected + ill)) + Constants.G

        if next_state > Constants.NUM_STATES - 1:
            next_state = Constants.NUM_STATES - 1

        return Cell(self.i, self.j, next_state)

    def display(self):
        index = floor(Constants.NUM_COLORS * self.state / Constants.NUM_STATES)
        return Constants.COLORS[index]


def initialize(i, j, width, height):
    state = floor(random.random() * Constants.NUM_STATES)
    return Cell(i, j, state)


if __name__ == "__main__":
    scail.run(initialize, lambda: None, settings)
