"""The wireworld cellular automaton, on a random map"""

from enum import Enum
import random

import pyscail as scail


class Constants:
    WIDTH = 200
    HEIGHT = 150
    CELL_SIZE = 4
    INITIAL_FPS = 8

    WIRE_EPICENTER_DENSITY = 0.001
    WIRE_DENSITY = 0.1

    ELECTRON_DENSITY = 0.0005


settings = (
    scail.Settings.default()
    .set_dimensions(Constants.WIDTH, Constants.HEIGHT, Constants.CELL_SIZE)
    .set_mutate(False)
)


class Colors:
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    black = (0, 0, 0)


class State(Enum):
    EMPTY = "empty"
    CONDUCTOR = "conductor"
    ELECTRON_HEAD = "electron head"
    ELECTRON_TAIL = "electron tail"


def make_wireworld(width: int, height: int):
    map = [[State.EMPTY for _ in range(height)] for _ in range(width)]
    num_epicenters = int(Constants.WIRE_EPICENTER_DENSITY * width * height)
    epicenters = [random_point(width, height) for _ in range(num_epicenters)]

    epicenter_pairs = []
    for i in range(num_epicenters):
        for j in range(i + 1, num_epicenters):
            epicenter_pairs.append((epicenters[i], epicenters[j]))

    wires_to_spawn = width * height * Constants.WIRE_DENSITY
    while wires_to_spawn > 0 and len(epicenter_pairs) > 0:
        pair = epicenter_pairs[int(random.random() * len(epicenter_pairs))]
        wires_expended = join_pair(pair, map)
        wires_to_spawn -= wires_expended
        epicenter_pairs.remove(pair)

    return map


def random_point(width, height):
    rx = int(random.random() * width)
    ry = int(random.random() * height)
    return (rx, ry)


def join_pair(pair, map):
    ((x1, y1), (x2, y2)) = pair
    map[x1][y1] = State.CONDUCTOR
    map[x2][y2] = State.CONDUCTOR

    minx, maxx = min(x1, x2), max(x1, x2)
    miny, maxy = min(y1, y2), max(y1, y2)

    wires_laid = 0

    for i in range(minx, maxx + 1):
        map[i][miny] = State.CONDUCTOR
        map[i][maxy] = State.CONDUCTOR
        wires_laid += 2

    for j in range(miny, maxy + 1):
        map[minx][j] = State.CONDUCTOR
        map[maxx][j] = State.CONDUCTOR
        wires_laid += 2

    return wires_laid


class Cell:
    transmission_map = {
        State.EMPTY: State.EMPTY,
        State.ELECTRON_HEAD: State.ELECTRON_TAIL,
        State.ELECTRON_TAIL: State.CONDUCTOR,
    }

    def __init__(self, i: int, j: int, state: State):
        self.i = i
        self.j = j
        self.state = state

    def next(self):
        if self.state != State.CONDUCTOR:
            next_state = Cell.transmission_map[self.state]
        else:
            num_neighboring_electrons = 0
            neighbors = scail.cells(
                scail.kernels.wrap_moore_neighborhood(
                    self.i, self.j, Constants.WIDTH, Constants.HEIGHT
                )
            )
            for neighbor in neighbors:
                if neighbor.state == State.ELECTRON_HEAD:
                    num_neighboring_electrons += 1

            if num_neighboring_electrons == 1 or num_neighboring_electrons == 2:
                next_state = State.ELECTRON_HEAD
            else:
                next_state = State.CONDUCTOR

        return Cell(self.i, self.j, next_state)

    def display(self):
        match (self.state):
            case State.EMPTY:
                return Colors.black
            case State.CONDUCTOR:
                return Colors.yellow
            case State.ELECTRON_HEAD:
                return Colors.blue
            case State.ELECTRON_TAIL:
                return Colors.red


map = make_wireworld(Constants.WIDTH, Constants.HEIGHT)


def initialize(i: int, j: int, width: int, height: int):
    state = map[i][j]
    if state == State.CONDUCTOR and random.random() < Constants.ELECTRON_DENSITY:
        state = State.ELECTRON_HEAD
    return Cell(i, j, state)


if __name__ == "__main__":
    scail.run(initialize, lambda: None, settings)
