from dataclasses import dataclass


class Constants:
    GAME_WIDTH = 200
    GAME_HEIGHT = 150
    CELL_SIZE = 4
    INITIAL_FPS = 2


@dataclass
class Settings:
    game_width: int
    game_height: int
    cell_size: int
    unpaused_fps: int
    paused: bool = False
    current_fps: int = Constants.INITIAL_FPS
    mouse_mode: bool = True  # Whether clicking a cell makes it alive or dead
