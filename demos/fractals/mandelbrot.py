from dataclasses import dataclass

import pyscail as scail


class Constants:
    REAL_LEFT_BOUND = -2
    REAL_RIGHT_BOUND = 1.5
    IMAGINARY_UP_BOUND = 1.5
    IMAGINARY_DOWN_BOUND = -2

    MAGNITUDE_CEILING = 2

    WIDTH = 800
    HEIGHT = 800
    CELL_SIZE = 1


class Globals:
    num_generations: int = 1

    @classmethod
    def update(cls):
        cls.num_generations += 1


settings = (
    scail.Settings.default()
    .set_dimensions(Constants.WIDTH, Constants.HEIGHT, Constants.CELL_SIZE)
    .set_mutate(True)
)


@dataclass
class State:
    z: complex
    c: complex
    lost: bool = False
    num_generation_alive: int = 0

    def next(self):
        """z(n+1) = z(n)^2 + c"""
        if self.lost:
            return

        self.num_generation_alive += 1
        self.lost = abs(self.z) > Constants.MAGNITUDE_CEILING
        self.z = self.z**2 + self.c

    def display(self):
        if not self.lost:
            return (0, 0, 0)

        # https://stackoverflow.com/questions/16500656/which-color-gradient-is-used-to-color-mandelbrot-in-wikipedia
        quotient = self.num_generation_alive / Globals.num_generations
        color = int(lerp(0, 255, quotient))
        if quotient > 0.5:
            return (color, 255, color)
        else:
            return (0, color, 0)


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

    return State(complex(cr, ci), complex(cr, ci))


def lerp(a, b, t):
    return a + (b - a) * t


if __name__ == "__main__":
    scail.run(initialize, Globals.update, settings)
