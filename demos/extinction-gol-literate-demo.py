# The first step is to import thr pyscail library
# If you don't have it, it is available on PyPI through pip
import pyscail as scail
import pyscail.kernels as kernels

import random

WIDTH = 200
HEIGHT = 150
CELL_SIZE = 4
EXTINCTION_GENERATIONS = 20


# Let's make the settings object
settings = (
    scail.Settings.default().set_dimensions(WIDTH, HEIGHT, CELL_SIZE).set_mutate(False)
)

# Thanks for watching!


# Let's create the initialization function
# What does it initialize? It must return a 2D list of a class that has the methods
# 'next' and 'display'. Next encapsulates the logic of how to get the next
# automaton state from the previous one, and display returns the color that the
# cell should have
class Cell:

    # Let's have an extinction event every 20 turns
    gens_till_extinction = EXTINCTION_GENERATIONS

    @classmethod
    def countdown(cls):
        cls.gens_till_extinction -= 1
        if cls.gens_till_extinction < 0:
            cls.gens_till_extinction = EXTINCTION_GENERATIONS

    # We are making Conway's game of life, with a twist
    def __init__(self, i: int, j: int, alive: bool, extinction: int) -> None:
        self.i, self.j, self.alive = i, j, alive
        self.extinction = extinction

    # in the next method, we will write the logic of conway's game of life
    # The way GOL works, all the next generation cells must first be computed before
    # the state can be changed. This mode of operation is called 'non-mutate' by scail,
    # and we will have to indicate that in the settings. For an example of mutable operation
    # check out the other examples
    def next(self):
        # scail provides helper functions to get the neighborhood of a point
        # see the kernels module for documentation
        # scail.cells converts indices to actual cells
        neighbors = scail.cells(
            kernels.wrap_moore_neighborhood(self.i, self.j, WIDTH, HEIGHT)
        )

        num_alive = 0
        for neighbor in neighbors:
            if neighbor.alive:
                num_alive += 1

        # Game of life ruleset
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

    # Returns the color of the cell
    def display(self):
        color_val = 255 if self.alive else 0
        # Just a visual indicator
        if self.extinction > 0:
            return (255, 0, 0)
        return (color_val, color_val, color_val)


# The initialization function
# It needs to have these four arguments
def initializer(i: int, j: int, width: int, height: int):
    # random starting position
    alive = True if random.random() > 0.5 else False
    return Cell(i, j, alive, 0)


# Each scail program runs by calling the run function
if __name__ == "__main__":
    # Run takes as parameters a function to initialize the grid of cells
    # A function that is run each generation
    # And a settings objecr
    #
    # For now we don't give an update function because we don't need to call anything every generation
    scail.run(initializer, Cell.countdown, settings)
