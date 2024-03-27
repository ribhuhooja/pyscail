import pygame

from settings import Settings, Constants
from graphics import Graphics
from grid import Grid
import kernels


class Scail:
    grid = None


def mainLoop(initialize, update, mutate: bool):
    """Initializes all the classes and then updates them in a loop until the game is over"""
    settings = Settings(
        Constants.GAME_WIDTH,
        Constants.GAME_HEIGHT,
        Constants.CELL_SIZE,
        Constants.INITIAL_FPS,
        paused=False,
    )
    settings.current_fps = settings.unpaused_fps

    grid = Grid(settings.game_width, settings.game_height, initialize, mutate)
    Scail.grid = grid
    clock = pygame.time.Clock()
    graphics = Graphics(settings)

    gameExit = False
    while not gameExit:
        clock.tick(settings.current_fps)

        if not settings.paused:
            grid.step_grid()
            update()

        graphics.render_grid(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                break


def run(initialize, update, mutate=True):
    """Runs the specified cellular automaton

    initialize - a function to initialize the grid,
    with parameters i, j, width, height

    update - a function that is run every generation. No parameters
    """
    pygame.init()
    pygame.display.set_caption("SCAIL")
    mainLoop(initialize, update, mutate)
    pygame.quit()


def cells(indices):

    return [Scail.grid.cells[i][j] for (i, j) in indices]
