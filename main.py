"""
Entrypoint for life-cli.

Initializes engine and launches TUI.
"""

import argparse
import csv
from engine import LifeEngine
import ui_terminal

def load_csv_matrix(path):
    matrix = []
    
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()

            if line:
                row = [int(x) for x in line.split(',')]
                matrix.append(row)

    return matrix

def main():
    parser = argparse.ArgumentParser(
        description="A terminal-based implementation of Conway's Game of Life."
    )
    
    parser.add_argument(
        "-W", "--width", 
        type=int, 
        default=None, 
        help="Width of the grid. Defaults to CSV width if provided, else 60"
    )
    
    parser.add_argument(
        "-H", "--height", 
        type=int, 
        default=None, 
        help="Height of the grid. Defaults to CSV width if provided, else 15"
    )

    parser.add_argument(
            "-i", "--input",
            type=str,
            default=None,
            help="Path to a CSV file representing the initial grid state (0s and 1s)"
    )
    
    args = parser.parse_args()

    matrix = None
    if args.input:
        matrix = load_csv_matrix(args.input)

    if matrix:
        width = args.width if args.width is not None else len(matrix[0])
        height = args.height if args.height is not None else len(matrix)
    else:
        width = args.width if args.width is not None else 60
        height = args.height if args.height is not None else 15

    if width < 1 or height < 1:
        parser.error("Grid dimensions must be strictly positive integers.")

    engine = LifeEngine(width, height)
    if matrix:
        engine.load_matrix(matrix)
    
    # Run
    ui_terminal.run(engine)

if __name__ == "__main__":
    main()
