# conway-game-of-life

A very simple implementation of John Conway's Game of Life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

This implements the game in a grid of 200x150 cells. While the classical implementation of Conway's game has an infinite grid,
this uses a finite grid that "wraps around" i.e. the first row is considered adjacent to the last row, and same for columns. 
Think a video game in which if you go too far off the edge in one direction, you come back from the edge in the other direction

This also allows "drawing" on the screen by editing which cells are alive and dead

Controls:
Spacebar - toggle pause and unpause
C - clear the screen i.e. kill all the cells
R - randomize all the cells
F - speed up
S - slow down
M - toggle mouse mode, whether clicking a cell makes it alive or dead

Mouse - Click on any cell to make it alive/dead. Drag the mouse while pressed to "draw" on the grid.
Try drawing your name and see how it evolves! Or try drawing the very simple r-pentomino, and see its chaotic nature:

XXXXX
XX**X
X**XX
XX*XX
XXXXX

(The asterisks represent alive cells, the Xs dead ones)

**Important notes**
The game starts out with no cells. To see the evolution, either press r for random generation, or draw something
Please only draw when paused, because otherwise the framerate might be too slow to have a satisfying drawing experience
(The framerate is kept slow to see the generations evolve. You can speed it up if you want to)

Since the game starts out unpaused, to draw something and see its effects, press space, draw, and then press space again

# Installation instructions
You will need python and pygame to run this program.