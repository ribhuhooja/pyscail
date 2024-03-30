"""Unit tests for the scail library, currently all in one file"""

import random

import kernels


def main():
    test_log(0, "beginning tests")
    test_kernels(100)

    test_log(0, "All tests passed successfully!")


def test_kernels(num_tests: int):
    test_log(1, "testing kernels")
    WIDTH = 100
    HEIGHT = 200
    for _ in range(num_tests):
        x = int(random.random() * WIDTH)
        y = int(random.random() * HEIGHT)

        test_wrap_moore(x, y, WIDTH, HEIGHT)
        test_nowrap_moore(x, y, WIDTH, HEIGHT)

    test_log(1, "Neighborhood kernel tests successfully passed")


def test_wrap_moore(x: int, y: int, width: int, height: int):
    neighbors = kernels.wrap_moore_neighborhood(x, y, width, height)
    assert len(neighbors) == 8

    for neighbor in neighbors:
        nx, ny = neighbor
        assert (x, y) != (nx, ny)
        assert nx == x or nx == (x + 1) % width or nx == (x - 1) % width
        assert ny == y or ny == (y + 1) % height or ny == (y - 1) % height


def test_nowrap_moore(x: int, y: int, width: int, height: int):
    neighbors = kernels.no_wrap_moore_neighborhood(x, y, width, height)

    length = len(neighbors)
    if x == 0 or x == width - 1:
        if y == 0 or y == height - 1:
            assert length == 3
        else:
            assert length == 5
    elif y == 0 or y == height - 1:
        assert length == 5
    else:
        assert length == 8

    for neighbor in neighbors:
        assert (x, y) != neighbor
        assert abs(x - neighbor[0]) <= 1
        assert abs(y - neighbor[1]) <= 1


def test_log(level: int, message: str):
    tabs = "  " * level
    print(tabs + message)


if __name__ == "__main__":
    main()
