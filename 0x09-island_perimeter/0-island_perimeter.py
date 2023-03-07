#!/usr/bin/python3
"""
0-island_countereter
"""


def island_perimeter(grid):
    """
    Arg: grid (list of lists)
    - for efficiency skip 1st and last row.
    - create variable counter
    - iterate through the i and increase counter when one is found
    Return counter once iteration complete.
    """
    if grid is None:
        return 0

    grid_height = len(grid)
    counter = 0
    for i in range(grid_height):
        grid_width = len(grid[i])
        for j in range(grid_width):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    counter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    counter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    counter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    counter += 1
    return counter
