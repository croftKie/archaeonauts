from enum import Enum

class State(Enum):
    MENU = 0
    IDLE = 1
    MOVE = 2
    ENTRY = 3
    PUZZLE = 4
    SHIP = 5

class PuzzleState(Enum):
    PUZZLE_ENTRY = 1
    PUZZLE_ACTIVE = 2
    PUZZLE_COMPLETE = 3
    PUZZLE_DEFEAT = 4

class MenuState(Enum):
    MENU_LOAD = "menu_load"
    MENU_ABOUT = "menu_about"
    MENU_NEW_GAME = "menu_new_game"
    MENU_LOAD_GAME = "menu_load_game"