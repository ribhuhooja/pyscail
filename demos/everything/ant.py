"""Langton's ant"""

from dataclasses import dataclass
from enum import Enum

import pyscail as scail
from settings import Direction, Constants, settings, BW


class Ant:
    x: int = Constants.ANT_START_X
    y: int = Constants.ANT_START_Y
    facing: Direction = Constants.ANT_START_DIRECTION

    @classmethod
    def move(cls):
        cell = scail.cells([(cls.x, cls.y)])[0].ant_component
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


@dataclass
class Cell:
    i: int
    j: int
    color: BW

    def next(self):
        return self

    def display(self):
        if (self.i, self.j) == (Ant.x, Ant.y):
            return (255, 0, 0)

        color_val = 255 if self.color == BW.WHITE else 0
        return (color_val, color_val, color_val)


def initialize(i, j, width, height):
    return Cell(i, j, BW.WHITE)


if __name__ == "__main__":
    scail.run(initialize, Ant.move, settings)
