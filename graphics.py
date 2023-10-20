import pygame
import random

from conwayGrid import Grid
from settings import Settings


class Graphics:
    def __init__(self, settings: Settings):
        self.__settings = settings
        self.__resolution_width = self.__settings.game_width * self.__settings.cell_size
        self.__resolution_height = (
            self.__settings.game_height * self.__settings.cell_size
        )
        self.__screen = pygame.display.set_mode(
            (self.__resolution_width, self.__resolution_height)
        )

    def render_grid(self, grid: Grid):
        self.__screen.fill((0, 0, 0))
        for i in range(grid.width):
            for j in range(grid.height):
                self.__render_cell(i, j, grid.cells[i][j].is_alive)

        pygame.display.update()

    # Renders a cell at position i,j
    # Its actual position depends on the resolution, which depends on the cell size
    def __render_cell(self, i: int, j: int, alive: bool):
        color = (255, 255, 255) if alive else (0, 0, 0)
        size = self.__settings.cell_size
        rect = (i * size, j * size, size, size)
        pygame.draw.rect(self.__screen, color, rect)
