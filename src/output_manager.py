import time
from src.constants.states import MenuState, PuzzleState, State
from src.constants.dialogue import menu_dialogue
from src.constants.styles import menu_styles
from rich.console import Console
from rich import spinner
import random

class OutputManager():
    def __init__(self, gameManager):
        self.gm = gameManager
        self.console = Console()

    def output_menu_dialogue(self):
        if self.gm.current_state == State.MENU:
            for idx, line in enumerate(menu_dialogue[self.gm.current_sub_state]):
                self.console.print(line, style = menu_styles[MenuState.MENU_LOAD][idx])

    def output_start_game_dialogue(self):
        if self.gm.current_state == State.MENU:

            previous_idx = [];

            for idx in range(0,3):
                length = len(menu_dialogue[MenuState.MENU_NEW_GAME])
                rand_dialogue = random.randint(0, length - 1)
                while rand_dialogue in previous_idx:
                    rand_dialogue = random.randint(0, length - 1)

                previous_idx.append(rand_dialogue)

                dialogue = menu_dialogue[MenuState.MENU_NEW_GAME][rand_dialogue]
                style = menu_styles[MenuState.MENU_NEW_GAME][0]
                self.__spawn_spinner(dialogue, "aesthetic", style, 0.5, 3)
            return True
                
    def output_start_game_lore(self):
        if self.gm.current_state == State.MENU:
            for idx, line in enumerate(menu_dialogue[MenuState.MENU_ABOUT]):
                self.console.print(line, style = menu_styles[MenuState.MENU_ABOUT][idx])
                self.console.print("")
                time.sleep(5)

    
    def output_map(self):
        return 
    

    ## Utilities

    def __spawn_spinner(self, dialogue, spinner, spinner_style, spinner_speed, spinner_duration):
        with self.console.status(dialogue, spinner=spinner, spinner_style=spinner_style, speed=spinner_speed):
            time.sleep(spinner_duration)