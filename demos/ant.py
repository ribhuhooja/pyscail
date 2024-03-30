"""Langton's ant"""

from dataclasses import dataclass
from enum import Enum

import pyscail as scail


class BW(Enum):
    BLACK = 0
    WHITE = 1


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    @staticmethod
    def clockwise(direction):
        match (direction):
            case Direction.UP:
                return Direction.RIGHT
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP
            case Direction.RIGHT:
                return Direction.DOWN

    @staticmethod
    def anti_clockwise(direction):
        match (direction):
            case Direction.UP:
                return Direction.LEFT
            case Direction.DOWN:
                return Direction.RIGHT
            case Direction.LEFT:
                return Direction.DOWN
            case Direction.RIGHT:
                return Direction.UP

    @staticmethod
    def forward_direction(direction):
        match (direction):
            case Direction.UP:
                return (0, -1)
            case Direction.DOWN:
                return (0, 1)
            case Direction.LEFT:
                return (-1, 0)
            case Direction.RIGHT:
                return (1, 0)


class Constants:
    SIMULATION_WIDTH = 200
    SIMULATION_HEIGHT = 150
    CELL_SIZE = 4
    INITIAL_FPS = 256

    ANT_START_X = 100
    ANT_START_Y = 75
    ANT_START_DIRECTION = Direction.RIGHT


class Ant:
    x: int = Constants.ANT_START_X
    y: int = Constants.ANT_START_Y
    facing: Direction = Constants.ANT_START_DIRECTION

    @classmethod
    def move(cls):
        cell = scail.cells([(cls.x, cls.y)])[0]
        if cell.color == BW.WHITE:
            Ant.facing = Direction.clockwise(Ant.facing)
            cell.color = BW.BLACK
            (dx, dy) = Direction.forward_direction(Ant.facing)
            Ant.x += dx
            Ant.y += dy
        else:
            Ant.facing = Direction.anti_clockwise(Ant.facing)
            cell.color = BW.WHITE
            (dx, dy) = Direction.forward_direction(Ant.facing)
            Ant.x += dx
            Ant.y += dy

        Ant.x %= Constants.SIMULATION_WIDTH
        Ant.y %= Constants.SIMULATION_HEIGHT


settings = (
    scail.Settings.default()
    .set_dimensions(
        Constants.SIMULATION_WIDTH, Constants.SIMULATION_HEIGHT, Constants.CELL_SIZE
    )
    .set_initial_fps(Constants.INITIAL_FPS)
    .set_mutate(True)
)


@dataclass
class Cell:
    i: int
    j: int
    color: BW

    def next(self):
        pass

    def display(self):
        if (self.i, self.j) == (Ant.x, Ant.y):
            return (255, 0, 0)

        color_val = 255 if self.color == BW.WHITE else 0
        return (color_val, color_val, color_val)


def initialize(i, j, width, height):
    return Cell(i, j, BW.WHITE)


if __name__ == "__main__":
    scail.run(initialize, Ant.move, settings)
