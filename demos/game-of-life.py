from dataclasses import dataclass

import pyscail as scail
import pyscail.kernels as kernels


class Constants:
    SIMULATION_WIDTH = 200
    SIMULATION_HEIGHT = 150
    CELL_SIZE = 4
    INITIAL_FPS = 8

    R_PENTOMINO = [(100, 100), (100, 101), (100, 99), (99, 100), (101, 99)]


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
    alive: bool

    def next(self):
        neighbors = scail.cells(
            kernels.wrap_moore_neighborhood(
                self.i,
                self.j,
                Constants.SIMULATION_WIDTH,
                Constants.SIMULATION_HEIGHT,
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
    # r-pentomino
    init_list = Constants.R_PENTOMINO
    alive = True if (i, j) in init_list else False
    return Cell(i, j, alive)


if __name__ == "__main__":
    scail.run(initialize, lambda: None, settings)
