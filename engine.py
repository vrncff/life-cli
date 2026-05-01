"""
Simulation engine.

Manages state, timing and interaction between core logic and UI.
"""
import core
import patterns

class LifeEngine:
    """
    Stateful controller for the Game of Life simulation.
    """
    def __init__(self, width, height):
        """
        Initialize simulation state and grid dimensions.
        """
        self.width = width
        self.height = height

        self.grid = core.create_empty(width,height)
        self.generation = 0

        self.paused = False
        self.editor_mode = False
        self.cursor_row = 0
        self.cursor_col = 0

        self.available_patterns = list(patterns.PATTERNS.items())
        self.current_pattern_idx = 0

        self.tick_interval = .15

    # Iterate
    def step(self):
        self.grid = core.step(self.grid, core.conway_rule)
        self.generation += 1

    # Control engine state
    def toggle_pause(self):
        self.paused = not self.paused

    def increase_speed(self):
        self.tick_interval = max(0.001, self.tick_interval - 0.10 * self.tick_interval)

    def decrease_speed(self):
        self.tick_interval += self.tick_interval * 0.05

    def toggle_editor(self):
        """
        Toggles editor mode. Entering editor mode pauses the simulation. Leaving it doesn't unpause the simulation.
        """
        if not self.paused and not self.editor_mode:
            self.toggle_pause()
        self.editor_mode = not self.editor_mode

    def toggle_cursor_cell(self):
        self.toggle_cells(self.cursor_row, self.cursor_col)

    def cycle_pattern(self, direction = 1): # +1 goes forward on list
        self.current_pattern_idx = (self.current_pattern_idx + direction) % len(self.available_patterns)

    # Grid management
    def set_random(self, alive_prob=0.3):
        self.grid = core.create_random(self.width, self.height, alive_prob)
        self.generation = 0

    def clear_grid(self):
        self.grid = core.create_empty(self.width, self.height)
        self.generation = 0

    # Grid editing
    def toggle_cells(self, row, col):
        pattern = self.available_patterns[self.current_pattern_idx][1]

        for dr, dc in pattern:
            r = (row + dr) % self.height
            c = (col + dc) % self.width
    
            self.grid[r][c] ^= 1

    def rotate_pattern(self):
        name, coords = self.available_patterns[self.current_pattern_idx]
        rotated_coords = [(dc, -dr) for dr, dc in coords]

        self.available_patterns[self.current_pattern_idx] = (name, rotated_coords)

    def move_cursor(self, dr, dc):
        self.cursor_row = (self.cursor_row + dr) % self.height
        self.cursor_col = (self.cursor_col + dc) % self.width

    def get_current_pattern(self):
        return self.available_patterns[self.current_pattern_idx][1]
