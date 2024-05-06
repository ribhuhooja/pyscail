import pyscail as scail
import pyscail.kernels as kernels

import random

from settings import Constants


settings = (
    scail.Settings.default()
    .set_dimensions(
        Constants.SIMULATION_WIDTH, Constants.SIMULATION_HEIGHT, Constants.CELL_SIZE
    )
    .set_mutate(False)
)


class Cell:

    gens_till_extinction = Constants.EXTINCTION_GENERATIONS

    @classmethod
    def countdown(cls):
        cls.gens_till_extinction -= 1
        if cls.gens_till_extinction < 0:
            cls.gens_till_extinction = Constants.EXTINCTION_GENERATIONS

    def __init__(self, i: int, j: int, alive: bool, extinction: int) -> None:
        self.i, self.j, self.alive = i, j, alive
        self.extinction = extinction

    def next(self):
        neighbors = scail.cells(
            kernels.wrap_moore_neighborhood(
                self.i, self.j, Constants.SIMULATION_WIDTH, Constants.SIMULATION_HEIGHT
            )
        )

        neighbors = [neighbor.extinction_component for neighbor in neighbors]

        num_alive = 0
        for neighbor in neighbors:
            if neighbor.alive:
                num_alive += 1

        if num_alive < 2 or num_alive > 3:
            next_alive = False
        elif num_alive == 3:
            next_alive = True
        else:
            next_alive = self.alive

        if Cell.gens_till_extinction == 0 and self.alive and num_alive < 3:
            self.extinction = 2
            next_alive = False

        if self.extinction > 0:
            self.extinction -= 1

        return Cell(self.i, self.j, next_alive, self.extinction)

    def display(self):
        color = (
            Constants.COLORS[0]
            if self.alive
            else Constants.COLORS[Constants.NUM_COLORS - 1]
        )
        # Just a visual indicator
        if self.extinction > 0:
            return (255, 0, 0)
        return color


def initialize(i: int, j: int, width: int, height: int):
    alive = True if random.random() > 0.5 else False
    return Cell(i, j, alive, 0)


if __name__ == "__main__":
    scail.run(initialize, Cell.countdown, settings)
