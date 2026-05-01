"""
Entrypoint for life-cli.

Initializes engine and launches TUI.
"""

import argparse
from engine import LifeEngine
import ui_terminal

def main():
    parser = argparse.ArgumentParser(
        description="A terminal-based implementation of Conway's Game of Life."
    )
    
    parser.add_argument(
        "-W", "--width", 
        type=int, 
        default=60, 
        help="Width of the grid (default: 60)"
    )
    
    parser.add_argument(
        "-H", "--height", 
        type=int, 
        default=15, 
        help="Height of the grid (default: 15)"
    )
    
    args = parser.parse_args()

    if args.width < 1 or args.height < 1:
        parser.error("Grid dimensions must be strictly positive integers.")

    engine = LifeEngine(args.width, args.height)
    
    # Run
    ui_terminal.run(engine)

if __name__ == "__main__":
    main()
