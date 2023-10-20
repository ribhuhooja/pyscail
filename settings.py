"""Provides Constants and Settings, some classes to hold data

Constants holds config data that doesn't change during execution
Settings holds data that needs to be shared between other classes and relates to the game settings and state
"""

from dataclasses import dataclass


class Constants:
    GAME_WIDTH = 200
    GAME_HEIGHT = 150
    CELL_SIZE = 4
    INITIAL_FPS = 2
    MAX_FPS = 128
    MIN_FPS = 1


@dataclass
class Settings:
    game_width: int
    game_height: int
    cell_size: int
    unpaused_fps: int  # The fps when the game is not paused
    paused: bool = False
    # The actual fps at which the screen updates. Needs to be separated from unpaused fps because
    # if fps is changed when the game is paused, its effects should take place after it is unpaused
    current_fps: int = Constants.INITIAL_FPS
    mouse_mode: bool = True  # Whether clicking a cell makes it alive or dead
