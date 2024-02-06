#!/usr/bin/python3

"""
Island Perimeter Module
"""


def island_perimeter(grid):
    """
    A function to calculate the perimeter of an Island

    Args:
     - Grid: A matrix representing the island

    Returns:
     - Perimeter: The perimeter of the island
    """
    perimeter = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if x < 0 or x >= len(grid) or y < 0 or y >= len(
                            grid[0]) or grid[x][y] == 0:
                        perimeter += 1
    return perimeter
