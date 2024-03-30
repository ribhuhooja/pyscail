"""Provides Constants and Settings, some classes to hold data

Constants holds config data that doesn't change during execution
Settings holds data that needs to be shared between other classes and relates to the game settings and state
"""

from dataclasses import dataclass
from typing import Self


class Defaults:
    GAME_WIDTH = 200  # Specified
    GAME_HEIGHT = 150  # Specified
    CELL_SIZE = 4  # optional
    INITIAL_FPS = 8  # optional
    MAX_FPS = 128  # optional
    MIN_FPS = 1  # optional
    MUTATE = False
    PAUSED = False


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
    # The actual fps at which the screen updates. Needs to be separated from unpaused fps because
    # if fps is changed when the game is paused, its effects should take place after it is unpaused
    current_fps: int
    paused: bool
    mutate: bool  # whether the autamaton does check-and-update or mutation

    @staticmethod
    def default():
        return Settings(
            Defaults.GAME_WIDTH,
            Defaults.GAME_HEIGHT,
            Defaults.CELL_SIZE,
            Defaults.INITIAL_FPS,
            Defaults.INITIAL_FPS,
            paused=Defaults.PAUSED,
            mutate=Defaults.MUTATE,
        )

    def set_dimensions(self, width: int, height: int, cell_size: int) -> Self:
        """Sets the dimensions of the program and returns the mutated object

        The resolution will be (width * cell_size) x (height * cell_size)
        """
        self.game_width = width
        self.game_height = height
        self.cell_size = cell_size
        return self

    def set_initial_fps(self, fps: int):
        """Sets the initial fps of the program and returns the mutated object

        FPS must be between 1 and 128, inclusive
        """

        self.current_fps = self.unpaused_fps = fps
        return self

    def set_mutate(self, mutate: bool):
        """Sets the mutate of the scail and returns the mutated object"""
        self.mutate = mutate
        return self

    def __str__(self) -> str:
        return f"Settings(width: {self.game_width}, height: {self.game_height}, cell_size = {self.cell_size}, ...)"
