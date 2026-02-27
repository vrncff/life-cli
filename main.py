"""
Entrypoint for life-cli.

Initializes engine and launches TUI.
"""
from engine import LifeEngine
import ui_terminal

def main():
    # Set grid size
    width = 60
    height = 15
    engine = LifeEngine(width, height)
    
    # Run
    ui_terminal.run(engine)

if __name__ == "__main__":
    main()
