"""Provides the Graphics class, which draws everything on the screen"""

import pygame

from grid import Grid, Cell
from settings import Settings, Constants


class Graphics:
    """Draws to and updates the screen"""

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
        """Draws the grid of cells onto the screen"""
        self.__screen.fill((0, 0, 0))
        for i in range(grid.width):
            for j in range(grid.height):
                self.__render_cell(i, j, grid.cells[i][j])

        # Update the screen so that the changes take place
        pygame.display.update()

    def __render_cell(self, i: int, j: int, cell: Cell):
        """Renders a cell at index i,j

        Its actual position depends on the resolution, which depends on the cell size
        So a cell of index (i,j) is rendered at (top corner) = (i*cell_size, j*cell_size)
        """

        color_val = 255 - int(255 * cell.numiters / cell.generations)
        color = (color_val, color_val, color_val)
        size = self.__settings.cell_size
        rect = (i * size, j * size, size, size)
        pygame.draw.rect(self.__screen, color, rect)
