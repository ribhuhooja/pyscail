from enum import Enum

import pyscail as scail


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
    SIMULATION_WIDTH = 80
    SIMULATION_HEIGHT = 60
    CELL_SIZE = 4
    INITIAL_FPS = 256

    ANT_START_X = 40
    ANT_START_Y = 30
    ANT_START_DIRECTION = Direction.RIGHT

    EXTINCTION_GENERATIONS = 20

    WIRE_EPICENTER_DENSITY = 0.001
    WIRE_DENSITY = 0.1
    ELECTRON_DENSITY = 0.0005

    REAL_LEFT_BOUND = -2
    REAL_RIGHT_BOUND = 1.5
    IMAGINARY_UP_BOUND = 1.5
    IMAGINARY_DOWN_BOUND = -2
    MAGNITUDE_CEILING = 2

    K1 = 2
    K2 = 3
    NUM_STATES_BZ = 200
    G = 70
    NUM_COLORS = 8
    COLORS = [(255 - i, 128 - i // 2, i) for i in range(0, 256, int(256 / NUM_COLORS))]

    NUM_STATES = 256


settings = (
    scail.Settings.default()
    .set_dimensions(
        Constants.SIMULATION_WIDTH, Constants.SIMULATION_HEIGHT, Constants.CELL_SIZE
    )
    .set_initial_fps(Constants.INITIAL_FPS)
    .set_mutate(False)
)


class BW(Enum):
    BLACK = 0
    WHITE = 1
