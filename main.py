import pygame

from conwayGrid import Grid
from graphics import Graphics
from settings import Settings, Constants


# handles inputs, and returns a boolean that is assigned to gameExit
def handle_inputs():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.WINDOWCLOSE:  # Alternate quit event
            return True

        return False


def mainLoop():
    settings = Settings(
        Constants.GAME_WIDTH,
        Constants.GAME_HEIGHT,
        Constants.CELL_SIZE,
        Constants.INITIAL_FPS,
    )
    grid = Grid(settings.game_width, settings.game_height)
    clock = pygame.time.Clock()
    graphics = Graphics(settings)

    gameExit = False
    while not gameExit:
        clock.tick(settings.fps)
        grid.step_grid()
        graphics.render_grid(grid)

        gameExit = handle_inputs()


def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    mainLoop()
    pygame.quit()


if __name__ == "__main__":
    main()
