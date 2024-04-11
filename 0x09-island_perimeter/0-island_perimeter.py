#!/usr/bin/python3
""" A function hat returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid (List[List[int]]):
    A list of lists of integers representing the island grid.
    0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.

    Constraints:
    - grid is rectangular, with its width and height not exceeding 100.
    - The grid is completely surrounded by water.
    - There is only one island (or nothing).
    - The island doesn’t have “lakes”
    (water inside that isn’t connected to the water surrounding the island).
    - Each cell is square, with a side length of 1.
    - Cells are connected horizontally/vertically (not diagonally).

    Example:
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    island_perimeter(grid) => 16
    """

    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
