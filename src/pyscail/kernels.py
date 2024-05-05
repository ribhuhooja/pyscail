"""A bunch of utility functions for getting neighborhoods"""

# This is a dirty trick that should be used carefully
saved_kernels = []
cache_kernels = False


def initialize_kernel_caching(width: int, height: int):
    global cache_kernels, saved_kernels
    cache_kernels = True
    saved_kernels = [None for _ in range(width * height)]


def no_wrap_moore_neighborhood(i, j, width, height):
    if cache_kernels:
        to_return = saved_kernels[width * j + i]
        if to_return is not None:
            return to_return

    result = []
    for x in range(max(i - 1, 0), min(i + 2, width)):
        for y in range(max(j - 1, 0), min(j + 2, height)):
            if (x, y) != (i, j):
                result.append((x, y))

    if cache_kernels:
        saved_kernels[width * j + i] = result

    return result


def wrap_moore_neighborhood(i, j, width, height):
    if cache_kernels:
        to_return = saved_kernels[width * j + i]
        if to_return is not None:
            return to_return

    result = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x, y) != (i, j):
                result.append((x % width, y % height))

    if cache_kernels:
        saved_kernels[width * j + i] = result

    return result


def wrap_von_neumann_neighborhood(i, j, width, height):
    if cache_kernels:
        to_return = saved_kernels[width * j + i]
        if to_return is not None:
            return to_return

    result = []
    result.append(((i + 1) % width, (j + 1) % height))
    result.append(((i - 1) % width, (j + 1) % height))
    result.append(((i + 1) % width, (j - 1) % height))
    result.append(((i - 1) % width, (j - 1) % height))

    if cache_kernels:
        saved_kernels[width * j + i] = result

    return result


def nowrap_von_neumann_neighborhood(i, j, width, height):
    if cache_kernels:
        to_return = saved_kernels[width * j + i]
        if to_return is not None:
            return to_return

    result = []
    for x, y in [(i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1), (i - 1, j - 1)]:
        if x >= 0 and x < width and y >= 0 and y < width:
            result.append((x, y))

    if cache_kernels:
        saved_kernels[width * j + i] = result

    return result
