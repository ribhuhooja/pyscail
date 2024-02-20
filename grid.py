"""Provides Grid, a class that holds all the cells"""

from dataclasses import dataclass
from typing import Tuple
from settings import Constants
from math import sqrt


@dataclass
class Cell:
    cr: float   # real part of the constant C
    ci: float   # imaginary part of the constant C
    zr: float   # real part of Z
    zi: float   # imaginary part of Z

    lost: bool = False  # gone above the overflow protection boundary

    def is_bounded(self):
        """
        Returns whether a cell is bounded or not, for displaying the set
        """
        if self.lost:
            return False

        magnitude = sqrt(self.zr**2 + self.zi**2)
        if (magnitude > Constants.OVERFLOW_PROTECTION):
            self.lost = True
            return False
        return magnitude < Constants.MAGNITUDE_CEILING

    def step(self):
        if self.lost:
            return

        self.zr, self.zi = z_squared_plus_c(self.zr, self.zi, self.cr, self.ci)


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells: list[list[Cell]] = self.initial_cells()

    def step_grid(self):
        """From the current generation of cells, produce the next one

        Unlike Conway, each cell depends only on itself.
        The update rule for each cell is Z(n+1) = Z(n)^2 + C,
        where Z(0) = 0 and C is the complex number associated
        with the cell.
        """
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].step()

    def reset(self):
        self.cells = self.initial_cells()


    def initial_cells(self) -> list[list[Cell]]:
        cells = [
            [Cell(lerp(Constants.REAL_LEFT_BOUND, Constants.REAL_RIGHT_BOUND, i/self.width),
                  lerp(Constants.IMAGINARY_DOWN_BOUND, Constants.IMAGINARY_UP_BOUND, j/self.height),
                  0,
                  0) for j in range(self.height)]
            for i in range(self.width)
        ]

        return cells


def z_squared_plus_c(zr: float, zi: float, cr: float, ci: float) -> Tuple[float, float]:
    """
    Does the complex number operation Z^2 + C
    """

    next_zr = zr**2 - zi**2 + cr
    next_zi = 2*zr*zi + ci

    return next_zr, next_zi


def lerp(min: float, max: float, percentage: float):
    """
    Linear interpolation
    """

    return min + percentage * (max - min)
