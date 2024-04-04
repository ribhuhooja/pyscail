from dataclasses import dataclass
from enum import Enum
import random

import pyscail as scail
import pyscail.kernels as kernels


class Constants:
    SIMULATION_WIDTH = 200
    SIMULATION_HEIGHT = 150
    CELL_SIZE = 4
    INITIAL_FPS = 8


settings = (
    scail.Settings.default()
    .set_dimensions(
        Constants.SIMULATION_WIDTH, Constants.SIMULATION_HEIGHT, Constants.CELL_SIZE
    )
    .set_initial_fps(Constants.INITIAL_FPS)
)


class State(Enum):
    ROCK = ("rock",)
    PAPER = ("paper",)
    SCISSORS = "scissors"


@dataclass
class Cell:
    i: int
    j: int
    state: State

    def next(self):
        neighbors = scail.cells(
            kernels.wrap_moore_neighborhood(
                self.i,
                self.j,
                Constants.SIMULATION_WIDTH,
                Constants.SIMULATION_HEIGHT,
            )
        )

        num_rock = num_paper = num_scissors = 0
        for cell in neighbors:
            match cell.state:
                case State.ROCK:
                    num_rock += 1
                case State.PAPER:
                    num_paper += 1
                case State.SCISSORS:
                    num_scissors += 1

        match self.state:
            case State.ROCK:
                next_state = State.ROCK if num_rock > num_paper else State.PAPER
            case State.PAPER:
                next_state = State.PAPER if num_paper > num_scissors else State.SCISSORS
            case State.SCISSORS:
                next_state = State.SCISSORS if num_scissors > num_rock else State.ROCK

        return Cell(self.i, self.j, next_state)

    def display(self):
        match self.state:
            case State.ROCK:
                return (0, 0, 128)
            case State.PAPER:
                return (0, 128, 0)
            case State.SCISSORS:
                return (128, 0, 0)


def initialize(i, j, width, height):
    rand = random.random()
    if rand < 0.33:
        state = State.ROCK
    elif rand < 0.66:
        state = State.PAPER
    else:
        state = State.SCISSORS
    return Cell(i, j, state)


if __name__ == "__main__":
    scail.run(initialize, lambda: None, settings)
