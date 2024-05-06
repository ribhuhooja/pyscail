import pyscail as scail

import random

import ant
import extinction
import wireworld
import mandelbrot
import rps
import bz
import grain
from settings import settings


NUM_MIXED = 7
INTERPOLATION_GENERATIONS = 1


def color_add(color_1, color_2):
    r = color_1[0] + color_2[0]
    g = color_1[1] + color_2[1]
    b = color_1[2] + color_2[2]
    return (r, g, b)


class Color:
    def __init__(self, tuple):
        self.r = tuple[0]
        self.g = tuple[1]
        self.b = tuple[2]

    def uncolor(self):
        return (self.r, self.g, self.b)

    def __add__(self, other):
        r = self.r + other.r
        if r > 255:
            r = 255

        g = self.g + other.g
        if g > 255:
            g = 255

        b = self.b + other.b
        if b > 255:
            b = 255
        return Color((r, g, b))

    def __mul__(self, other: float | int):
        r = int(other * self.r)
        g = int(other * self.g)
        b = int(other * self.b)

        if r > 255:
            r = 255

        if g > 255:
            g = 255

        if b > 255:
            b = 255

        return Color((other * self.r, other * self.g, other * self.b))

    __rmul__ = __mul__


class Cell:
    def __init__(
        self,
        ant_component,
        extinction_component,
        wireworld_component,
        mandelbrot_component,
        rps_component,
        bz_component,
        grain_component,
    ):
        self.ant_component = ant_component
        self.extinction_component = extinction_component
        self.wireworld_component = wireworld_component
        self.mandelbrot_component = mandelbrot_component
        self.rps_component = rps_component
        self.bz_component = bz_component
        self.grain_component = grain_component

    def next(self):
        next_ant = self.ant_component.next()
        next_extinction = self.extinction_component.next()
        next_wire = self.wireworld_component.next()
        next_mand = self.mandelbrot_component.next()
        next_rps = self.rps_component.next()
        next_bz = self.bz_component.next()
        next_grain = self.grain_component.next()

        return Cell(
            next_ant,
            next_extinction,
            next_wire,
            next_mand,
            next_rps,
            next_bz,
            next_grain,
        )

    def display(self):
        ant_display = self.ant_component.display()
        extinction_display = self.extinction_component.display()
        wire_display = self.wireworld_component.display()
        mand_display = self.mandelbrot_component.display()
        rps_display = self.rps_component.display()
        bz_display = self.bz_component.display()
        grain_display = self.grain_component.display()
        return (
            Globals.display_array[0] * Color(ant_display)
            + Globals.display_array[1] * Color(extinction_display)
            + Globals.display_array[2] * Color(wire_display)
            + Globals.display_array[3] * Color(mand_display)
            + Globals.display_array[4] * Color(rps_display)
            + Globals.display_array[5] * Color(bz_display)
            + Globals.display_array[6] * Color(grain_display)
        ).uncolor()


def generate_random_display_array(num_elements, *biases):
    biases_padded = [biases[i] if i < len(biases) else 0 for i in range(num_elements)]
    arr = [random.random() + biases_padded[i] for i in range(num_elements)]
    normalization_factor = sum(arr)
    arr = [i / normalization_factor for i in arr]
    return arr


class Globals:
    display_array = generate_random_display_array(NUM_MIXED, 0, 0, 0, 0, 0, 0, 30)
    previous_display_array = [i for i in display_array]
    target_display_array = generate_random_display_array(NUM_MIXED)
    interpolation_progress = 0

    @classmethod
    def global_update(cls):
        ant.Ant.move()

        cls.interpolation_progress += 1
        if cls.interpolation_progress == INTERPOLATION_GENERATIONS:
            cls.interpolation_progress = 0
            cls.previous_display_array = cls.target_display_array
            cls.target_display_array = generate_random_display_array(NUM_MIXED)

        t = cls.interpolation_progress / INTERPOLATION_GENERATIONS
        cls.display_array = [
            a + t * (b - a)
            for (a, b) in zip(cls.previous_display_array, cls.target_display_array)
        ]


def initialize(i, j, width, height):
    ant_component = ant.initialize(i, j, width, height)
    extinction_component = extinction.initialize(i, j, width, height)
    wire_component = wireworld.initialize(i, j, width, height)
    mandelbrot_component = mandelbrot.initialize(i, j, width, height)
    rps_component = rps.initialize(i, j, width, height)
    bz_component = bz.initialize(i, j, width, height)
    grain_component = grain.initialize(i, j, width, height)
    return Cell(
        ant_component,
        extinction_component,
        wire_component,
        mandelbrot_component,
        rps_component,
        bz_component,
        grain_component,
    )


if __name__ == "__main__":
    scail.run(initialize, Globals.global_update, settings)
