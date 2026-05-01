# Patterns expressed as active cells in relative coordinates to the top left corner of the pattern
CELL = [
    (0,0),
]

GLIDER = [
    (1,0),
    (2,1),
    (0,2),
    (1,2),
    (2,2),
]

BLINKER = [
    (0,0),
    (0,1),
    (0,2)
]

BLOCK = [
    (0,0),
    (0,1),
    (1,0),
    (1,1)
]

TOAD = [
    (0,1),
    (0,2),
    (0,3),
    (1,0),
    (1,1),
    (1,2)
]

BEACON = [
    (0,0),
    (0,1),
    (1,0),
    (1,1),
    (2,2),
    (2,3),
    (3,2),
    (3,3)
]

# dict
PATTERNS = {
    "cell": CELL,
    "glider": GLIDER,
    "blinker": BLINKER,
    "block": BLOCK,
    "toad": TOAD,
    "beacon": BEACON,
}
