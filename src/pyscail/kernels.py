"""A bunch of utility functions for getting neighborhoods"""


def no_wrap_moore_neighborhood(i, j, width, height):
    result = []
    for x in range(max(i - 1, 0), min(i + 2, width)):
        for y in range(max(j - 1, 0), min(j + 2, height)):
            if (x, y) != (i, j):
                result.append((x, y))

    return result


def wrap_moore_neighborhood(i, j, width, height):
    result = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x, y) != (i, j):
                result.append((x % width, y % height))

    return result
