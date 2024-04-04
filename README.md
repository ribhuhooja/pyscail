# pyscail

**pyscail** is a package for creating cellular automata. It allows you to specify the
allowed states, and the transitions between them, and does everything else for you

## Installation

You need to have python (>= 3.11) installed on your system. Once you have that,
you can:

```bash
pip install pyscail
```

(or `pip3`, depending on your system)

## Usage

## Demos
See the following video for a demonstration on how to write code using this
library.

See the demos folder for a lot more (and more varied) examples on how to use the 
library. Written demo automata include:

- Conway's game of life
- The modified game of life with extinction, in demo.py 
- Langton's ant 
- Wireworld
- Rock-Paper-Scissors automata 
- Belusov-Zhabotinsky reaction
- the Mandelbrot and Julia sets

## Other

### Kernel Caching
Kernel caching is an option you can enable through `kernels.initialize_kernel_caching`
If this is set, then instead of being calculated every frame, the neighborhoods
of a given point will be calculated once then cached. This will probably
not cause any issues unless you change your neighborhood strategy mid-simulation.

Still, I didn't notice a significant speedup upon implementing caching, so for now
it is just an option that is turned off by default.
