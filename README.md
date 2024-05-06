# pyscail

**pyscail** is a package for creating cellular automata. It allows you to specify the
allowed states, and the transitions between them, and does everything else for you

![rock-paper-scissors gif](media/rps-gif.gif)

## Installation

You need to have python (>= 3.11) installed on your system. Once you have that,
you can:

```bash
pip install pyscail
```

(or `pip3`, depending on your system)

## Usage
See this video for a demonstration of how to use the library: 
https://youtu.be/BjPNs30i2TQ

A brief summary - provide a class with a `next` method and a 
`display` method. Provide a initialization function that returns
an instance of your class given some coordinates. Provide a settings
object that you can make using method provided by the library.
Optionally, provide a function that will be called once each generation.

Then, simply call `scail.run` to run the ruleset.


![Belusov-Zhabotinsky gif](media/bz-gif.gif)

## Demos
See the following video for a demonstration on how to write code using this
library.

See the demos folder for a lot more (and more varied) examples on how to use the 
library. Written demo automata include:

- Conway's game of life
- The modified game of life with extinction, in demo.py 
- Langton's ant 
![Langton gif](media/langton-gif.gif)
- Wireworld
- Rock-Paper-Scissors automata 
- Belusov-Zhabotinsky reaction
- the Mandelbrot and Julia sets

And lastly, this demo of many of the above rulesets combined into one 
ruleset and run all together, then displayed as a weighted average
![everything gif](media/everything-gif.gif)

## Other

### Kernel Caching
Kernel caching is an option you can enable through `kernels.initialize_kernel_caching`
If this is set, then instead of being calculated every frame, the neighborhoods
of a given point will be calculated once then cached. This will probably
not cause any issues unless you change your neighborhood strategy mid-simulation.

Still, I didn't notice a significant speedup upon implementing caching, so for now
it is just an option that is turned off by default.
