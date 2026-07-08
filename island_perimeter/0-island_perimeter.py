#!/usr/bin/python3
"""
Module 0-island_perimeter
Determines the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    Return the perimeter of the island described in grid.

    Args:
        grid (list): list of list of integers where
                     0 represents water and 1 represents land

    Returns:
        int: the perimeter of the island
    """
    perimeter = 0
    height = len(grid)

    for row in range(height):
        width = len(grid[row])
        for col in range(width):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
