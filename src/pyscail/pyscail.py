import pygame

from pyscail.settings import Settings
from pyscail.graphics import Graphics
from pyscail.grid import Grid


class Scail:
    grid: Grid | None = None


def mainLoop(initialize, update, settings: Settings):
    """Initializes all the classes and then updates them in a loop until the game is over"""

    settings.current_fps = settings.unpaused_fps
    grid = Grid(settings.game_width, settings.game_height, initialize, settings.mutate)
    Scail.grid = grid
    clock = pygame.time.Clock()
    graphics = Graphics(settings)

    gameExit = False
    while not gameExit:
        clock.tick(settings.current_fps)

        graphics.render_grid(grid)
        if not settings.paused:
            grid.step_grid()
            update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                break


def run(initialize, update, settings: Settings):
    """Runs the specified cellular automaton

    initialize - a function to initialize the grid,
    with parameters i, j, width, height

    update - a function that is run every generation. No parameters
    """

    pygame.init()
    pygame.display.set_caption("SCAIL")
    mainLoop(initialize, update, settings)
    pygame.quit()


def cells(indices):

    return [Scail.grid.cells[i][j] for (i, j) in indices]
