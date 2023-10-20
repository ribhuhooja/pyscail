import pygame

from conwayGrid import Grid
from graphics import Graphics
from settings import Settings, Constants


# handles inputs, and returns a boolean that is assigned to gameExit
# takes in a Settings object and a Grid object that it mutates
# depending on the inputs
def handle_inputs(settings: Settings, grid: Grid):
    # Handling window closing and key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.WINDOWCLOSE:  # Alternate quit event
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not settings.paused:
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
                if settings.unpaused_fps < 128:
                    settings.unpaused_fps *= 2
                    if not settings.paused:
                        settings.current_fps = settings.unpaused_fps
            elif event.key == pygame.K_s:
                if settings.unpaused_fps > 1:
                    settings.unpaused_fps //= 2
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
    pygame.init()
    pygame.display.set_caption("Game of Life")
    mainLoop()
    pygame.quit()


if __name__ == "__main__":
    main()
