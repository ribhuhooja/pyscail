import pygame

from settings import Settings, Constants
from graphics import Graphics


class Grid:
    def __init__(self, width, height, initialize):
        self.width = width
        self.height = height
        self.initialize = initialize
        self.cells = self.initial_cells()

    def step_grid(self):
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].next()

    def reset(self):
        self.cells = self.initial_cells()

    def initial_cells(self):
        cells = [
            [self.initialize(i, j, self.width, self.height) for j in range(self.height)]
            for i in range(self.width)
        ]

        return cells


def mainLoop(initialize):
    """Initializes all the classes and then updates them in a loop until the game is over"""
    settings = Settings(
        Constants.GAME_WIDTH,
        Constants.GAME_HEIGHT,
        Constants.CELL_SIZE,
        Constants.INITIAL_FPS,
        paused=False,
    )
    settings.current_fps = settings.unpaused_fps

    grid = Grid(settings.game_width, settings.game_height, initialize)
    clock = pygame.time.Clock()
    graphics = Graphics(settings)

    gameExit = False
    while not gameExit:
        clock.tick(settings.current_fps)

        if not settings.paused:
            grid.step_grid()

        graphics.render_grid(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                break


def run(initialize):
    pygame.init()
    pygame.display.set_caption("SCAIL")
    mainLoop(initialize)
    pygame.quit()
