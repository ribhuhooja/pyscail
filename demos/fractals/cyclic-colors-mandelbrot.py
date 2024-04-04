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


class Colors:
    # https://stackoverflow.com/a/16505538/21005659
    mapping = [
        (66, 30, 15),
        (25, 7, 26),
        (9, 1, 47),
        (4, 4, 73),
        (0, 7, 100),
        (12, 44, 138),
        (24, 82, 177),
        (57, 125, 209),
        (134, 181, 229),
        (211, 236, 248),
        (241, 233, 191),
        (248, 201, 95),
        (255, 170, 0),
        (204, 128, 0),
        (153, 87, 0),
        (106, 52, 3),
    ]


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
        if self.lost:
            return Colors.mapping[self.num_generation_alive % 16]
        return (0, 0, 0)


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
