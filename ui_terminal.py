"""
Handles rendering and keyboard interaction for the Game of Life simulation.
"""
import sys
import termios
import tty
import select
import time
import os

# Helper functions for TUI
def get_key_nonblocking():
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if dr:
        return sys.stdin.read(1)

    return None

def setup_terminal():
    fd = sys.stdin.fileno()
    former_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)

    return fd, former_settings

def restore_terminal(fd, former_settings):
    termios.tcsetattr(fd, termios.TCSADRAIN, former_settings)

# Rendering TUI
def render(engine):
    os.system("clear")
    
    print("[SPACE] Pause | [+/-] Speed | [r] Random | [e] Toggle edit | [q] Quit" if not engine.editor_mode 
          else "[SPACE] Toggle cell | [h/j/k/l] Move cursor | [e] Toggle edit | [q] Quit")
    print(f"Generation: {engine.generation}")
    print(f"Interval: {engine.tick_interval:.3f}s")
    print("PAUSED" if engine.paused else "")
    print()

    for r, row in enumerate(engine.grid):
        print("". join(
            "▓" if engine.editor_mode and r == engine.cursor_row and c == engine.cursor_col and cell # if cursor over active cell
            else "░" if engine.editor_mode and r == engine.cursor_row and c == engine.cursor_col # if cursor over inactive cell
            else "█" if cell # active cell
            else " " # inactive cell
            for c, cell in enumerate(row)
            ))

# Handling input
def handle_normal_input(engine, key):
    """
    Map keyboard input to engine commands modally. (non-editing mode)
    """
    commands = {
        " ": engine.toggle_pause,
        "r": engine.set_random,
        "+": engine.increase_speed,
        "-": engine.decrease_speed,
        "e": engine.toggle_editor,
    }

    if key == "q":
        raise KeyboardInterrupt

    action = commands.get(key)
    if action:
        action()

def handle_editor_input(engine, key):
    """
    Map keyboard input to engine commands modally. (editing mode)
    """
    commands = {
        "h": lambda: engine.move_cursor(0,-1),
        "j": lambda: engine.move_cursor(1,0),
        "k": lambda: engine.move_cursor(-1,0),
        "l": lambda: engine.move_cursor(0,1),
        " ": engine.toggle_cursor_cell,
        "e": engine.toggle_editor,
    }

    if key == "q":
        raise KeyboardInterrupt

    action = commands.get(key)
    if action:
        action()

# Main loop
def main_loop(engine):
    while True:
        key = get_key_nonblocking()
        if key:
            if engine.editor_mode:
                handle_editor_input(engine,key)
            else:
                handle_normal_input(engine, key)

        if not engine.paused:
            engine.step()

        render(engine)
        time.sleep(engine.tick_interval)

# Run UI
def run(engine):
    """
    Start main loop and bind input to engine actions.
    """
    fd, former_settings = setup_terminal()

    try:
        main_loop(engine)

    except KeyboardInterrupt:
        pass

    finally:
        restore_terminal(fd, former_settings)
        os.system("clear")
