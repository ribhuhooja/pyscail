import pyscail as scail
import pyscail.kernels as kernels

import random


class Constants:
    WIDTH = 200
    HEIGHT = 150
    CELL_SIZE = 4

    GENERATIONS_TILL_EXTINCTION = 20


settings = (
    scail.Settings.default()
    .set_dimensions(Constants.WIDTH, Constants.HEIGHT, Constants.CELL_SIZE)
    .set_mutate(False)
)


class Cell:
    gens_till_extinction = Constants.GENERATIONS_TILL_EXTINCTION

    @classmethod
    def countdown(cls):
        cls.gens_till_extinction -= 1
        if cls.gens_till_extinction < 0:
            cls.gens_till_extinction = Constants.GENERATIONS_TILL_EXTINCTION

    def __init__(self, i: int, j: int, alive: bool, extinct: int = 0) -> None:
        self.i, self.j, self.alive = i, j, alive
        self.extinct = extinct

    def next(self):
        neighbors = scail.cells(
            kernels.wrap_moore_neighborhood(
                self.i, self.j, Constants.WIDTH, Constants.HEIGHT
            )
        )

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
            self.extinct = 2
            next_alive = False

        if self.extinct > 0:
            self.extinct -= 1

        return Cell(self.i, self.j, next_alive, self.extinct)

    def display(self):
        color_value = 255 if self.alive else 0
        if self.extinct > 0:
            print("called")
            return (255, 0, 0)
        return (color_value, color_value, color_value)


def initializer(i, j, width, height):
    alive = True if random.random() > 0.5 else False
    return Cell(i, j, alive)


if __name__ == "__main__":
    scail.run(initializer, Cell.countdown, settings)
