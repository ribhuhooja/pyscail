"""Executes all the code and calls upon all other modules"""

import pygame

from conwayGrid import Grid
from graphics import Graphics
from settings import Settings, Constants


def handle_inputs(settings: Settings, grid: Grid):
    """Handles inputs

    Returns a boolean that is assigned to gameExit and takes in a Settings object and a Grid object
    that it mutates depending on the inputs
    """

    # Handling window closing and key presses
    for event in pygame.event.get():
        # Quit event, when the window cross key is pressed
        if event.type == pygame.QUIT:
            # Sets gameExit to true, which ends the program
            return True
        elif event.type == pygame.WINDOWCLOSE:  # Alternate quit event
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not settings.paused:
                    # Faster FPS when paused for better drawing on the screen
                    settings.current_fps = 120
                    settings.paused = True
                else:
                    settings.current_fps = settings.unpaused_fps
                    settings.paused = False
            elif event.key == pygame.K_m:
                settings.mouse_mode = not settings.mouse_mode
            elif event.key == pygame.K_c:
                grid.clear()
            elif event.key == pygame.K_r:
                grid.randomize()
            elif event.key == pygame.K_f:
                if settings.unpaused_fps < Constants.MAX_FPS:
                    settings.unpaused_fps *= 2
                    # If unpaused, update the current fps
                    # If paused then this will happen during the unpausing
                    if not settings.paused:
                        settings.current_fps = settings.unpaused_fps
            elif event.key == pygame.K_s:
                # Can't have an fps lower than 1
                if settings.unpaused_fps > max(1, Constants.MIN_FPS):
                    settings.unpaused_fps //= 2  # FPS must be an integer
                    if not settings.paused:
                        settings.current_fps = settings.unpaused_fps

    # Now to handle the mouse
    if pygame.mouse.get_pressed()[0]:  # If LMB is pressed
        i, j = pygame.mouse.get_pos()

        # To get the cell index, divide its position by the cell size
        i //= settings.cell_size
        j //= settings.cell_size

        grid.cells[i][j].is_alive = settings.mouse_mode

        return False


def mainLoop():
    """Initializes all the classes and then updates them in a loop until the game is over"""
    settings = Settings(
        Constants.GAME_WIDTH,
        Constants.GAME_HEIGHT,
        Constants.CELL_SIZE,
        Constants.INITIAL_FPS,
        paused=False,
    )
    settings.current_fps = settings.unpaused_fps

    grid = Grid(settings.game_width, settings.game_height)
    clock = pygame.time.Clock()
    graphics = Graphics(settings)

    gameExit = False
    while not gameExit:
        clock.tick(settings.current_fps)

        if not settings.paused:
            grid.step_grid()

        graphics.render_grid(grid)

        gameExit = handle_inputs(settings, grid)


def main():
    """Executes all the code"""
    pygame.init()
    pygame.display.set_caption("Game of Life")
    mainLoop()
    pygame.quit()


if __name__ == "__main__":
    main()
