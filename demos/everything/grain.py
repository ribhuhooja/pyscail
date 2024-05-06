from dataclasses import dataclass
import math
import random

import pyscail as scail
import pyscail.kernels as kernels

from settings import Constants

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

        neighbors = [neighbor.grain_component for neighbor in neighbors]

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
        return Constants.COLORS[
            int(self.state * Constants.NUM_COLORS / Constants.NUM_STATES)
        ]


def initialize(i, j, width, height):
    state = math.floor(random.random() * (Constants.NUM_STATES))
    return Cell(i, j, state)


if __name__ == "__main__":
    scail.run(initialize, lambda: None, settings)
