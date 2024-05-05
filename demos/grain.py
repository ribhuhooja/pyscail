from dataclasses import dataclass
import math
import random

import pyscail as scail
import pyscail.kernels as kernels


class Constants:
    SIMULATION_WIDTH = 200
    SIMULATION_HEIGHT = 200
    CELL_SIZE = 4
    INITIAL_FPS = 16

    NUM_STATES = 256


settings = (
    scail.Settings.default()
    .set_dimensions(
        Constants.SIMULATION_WIDTH, Constants.SIMULATION_HEIGHT, Constants.CELL_SIZE
    )
    .set_initial_fps(Constants.INITIAL_FPS)
    .set_mutate(False)
)


@dataclass
class Cell:
    i: int
    j: int
    state: int

    def next(self):
        neighbors = scail.cells(
            kernels.wrap_von_neumann_neighborhood(
                self.i,
                self.j,
                Constants.SIMULATION_WIDTH,
                Constants.SIMULATION_HEIGHT,
            )
        )

        states = []
        for cell in neighbors:
            states.append(cell.state)

        unique_states = dict()
        for state in states:
            if state in unique_states:
                unique_states[state] += 1
            else:
                unique_states[state] = 1

        next_state = -1
        for state, num in unique_states.items():
            if num >= 3 and self.state == state:
                next_state = state

        if next_state == -1:
            random_index = math.floor(random.random() * len(states))
            next_state = states[random_index]

        return Cell(self.i, self.j, next_state)

    def display(self):
        red_val = math.floor(110 * self.state / Constants.NUM_STATES)
        green_val = math.floor(128 * self.state / Constants.NUM_STATES)
        blue_val = math.floor(128 * self.state / Constants.NUM_STATES)
        return (red_val, green_val, blue_val)


def initialize(i, j, width, height):
    state = math.floor(random.random() * (Constants.NUM_STATES))
    return Cell(i, j, state)


if __name__ == "__main__":
    scail.run(initialize, lambda: None, settings)
