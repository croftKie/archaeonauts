import time
from src.constants.states import MenuState, PuzzleState, State
from src.constants.dialogue import menu_dialogue
from src.constants.styles import menu_styles
from rich.console import Console
from rich import spinner
import random

from src.utilities.ascii import generate_title_art

class OutputManager():
    def __init__(self, gameManager):
        self.gm = gameManager
        self.console = Console()

    ##
    ##
    ## Menu Outputs
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
                self.__type_output(line, menu_styles[MenuState.MENU_ABOUT][idx], interval=0.05)
                self.console.print("\n")
                time.sleep(3)

    def output_load_game_dialogue(self):
        if self.gm.current_state == State.MENU:
            title = generate_title_art("Loading Save File")
            self.console.print(title)
            for idx, line in enumerate(menu_dialogue[MenuState.MENU_LOAD_GAME]):
                self.__type_output(line, menu_styles[MenuState.MENU_LOAD_GAME][idx], interval=0.05)
                self.console.print("\n")
                time.sleep(3)

    def output_about_menu_lore(self):
        if self.gm.current_state == State.MENU:
            title = generate_title_art("About Archeonauts")
            self.console.print(title)
            for idx, line in enumerate(menu_dialogue[MenuState.MENU_ABOUT]):
                self.__type_output(line, menu_styles[MenuState.MENU_ABOUT][idx], interval=0.05)
                self.console.print("\n")
                time.sleep(3)
    
    def output_quit_game_dialogue(self):
        if self.gm.current_state == State.MENU:
            title = generate_title_art("Returning to Earth")
            self.console.print(title)
            for idx, line in enumerate(menu_dialogue[MenuState.MENU_QUIT_GAME]):
                self.__type_output(line, menu_styles[MenuState.MENU_QUIT_GAME][idx], interval=0.05)
                self.console.print("\n")
                time.sleep(3)
    
    
    ##
    ##
    ## In Game Outputs
    
    def output_map(self):
        mm = self.gm.map_manager
        for i, row in enumerate(mm.gen_map):
            self.console.print("".join(row))
            if len(mm.gen_map) - 1 == i:
                self.console.print("")
            else:
                self.console.print(mm.connection_line)
    

    ## Utilities
    def __spawn_spinner(self, dialogue, spinner, spinner_style, spinner_speed, spinner_duration):
        with self.console.status(dialogue, spinner=spinner, spinner_style=spinner_style, speed=spinner_speed):
            time.sleep(spinner_duration)

    def __type_output(self, line, style, interval= 0.05,):
        for char in line:
            self.console.print(char, style = style, end="")
            time.sleep(interval)