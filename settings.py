"""Provides Constants and Settings, some classes to hold data

Constants holds config data that doesn't change during execution
Settings holds data that needs to be shared between other classes and relates to the game settings and state
"""

from dataclasses import dataclass


class Constants:
    GAME_WIDTH = 800  # Specified
    GAME_HEIGHT = 600  # Specified
    CELL_SIZE = 1  # optional
    INITIAL_FPS = 8  # optional
    MAX_FPS = 128  # optional
    MIN_FPS = 1  # optional


# Maybe the scail-specific constants can go in globals, or just a "Constants" class
#
# For the Settings class, the user can maybe define another settings class, and we can do a
# hasattr analysis


# None of these are scail-specific, so they will come from the "Settings constants"
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
