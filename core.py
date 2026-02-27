"""
Logic for Conway's Game of Life.

Stateless functions for grid creation, neighbor counting and rule application.
"""
import random

def create_empty(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]

# Create a random grid
def create_random(width, height, alive_prob=0.15):
    return [
        [1 if random.random() < alive_prob else 0 for _ in range(width)] for _ in range(height)
    ]

# Count cell neighbors
def count_neighbors(grid, x, y):
    """
    Count alive neighbors of a cell using toroidal wrapping.
    """
    w = len(grid[0])
    h = len(grid)

    count = 0

    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            
            # Toroidal wrapping
            nx = (x + dx) % w
            ny = (y + dy) % h
            count += grid[ny][nx]

    return count

# Classic Conway's Game of Life rule
def conway_rule(cell, neighbors):
    if cell == 1:
        return 1 if neighbors in (2,3) else 0
    else:
        return 1 if neighbors == 3 else 0

# Iterate on grid
def step(grid, rule):
    """
    Compute next generation without mutating the input grid. Returns a new grid.
    """
    h = len(grid)
    w = len(grid[0])

    new_grid = create_empty(w,h) # Create new grid to avoid mutating the current generation in-place

    for y in range(h):
        for x in range(w):
            neighbors = count_neighbors(grid, x, y)
            new_grid[y][x] = rule(grid[y][x], neighbors)

    return new_grid
