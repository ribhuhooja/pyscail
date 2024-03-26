from dataclasses import dataclass

import pyscail as scail


class Constants:
    REAL_LEFT_BOUND = -2
    REAL_RIGHT_BOUND = 1.5
    IMAGINARY_UP_BOUND = 1.5
    IMAGINARY_DOWN_BOUND = -1.5

    MAGNITUDE_CEILING = 2


@dataclass
class State:
    z: complex
    c: complex
    lost: bool

    def next(self):
        """z(n+1) = z(n)^2 + c"""
        if self.lost:
            return

        self.lost = abs(self.z) > Constants.MAGNITUDE_CEILING
        self.z = self.z**2 + self.c

    def display(self):
        color_val = 255 if self.lost else 0
        return (color_val, color_val, color_val)


def initialize(i, j, width, height):
    cr = lerp(
        Constants.REAL_LEFT_BOUND,
        Constants.REAL_RIGHT_BOUND,
        i / width,
    )

    ci = lerp(
        Constants.IMAGINARY_DOWN_BOUND,
        Constants.IMAGINARY_UP_BOUND,
        j / height,
    )

    return State(0, complex(cr, ci), False)


def lerp(a, b, t):
    return a + (b - a) * t


if __name__ == "__main__":
    scail.run(initialize)
