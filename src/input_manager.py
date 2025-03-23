from src.constants.dialogue import input_dialogue
from src.constants.states import State, MenuState
from src.constants.input_content import input_content
from src.constants.states import MenuState, PuzzleState, State

import inquirer
class InputManager():
    def __init__(self, gm):
        self.game = gm
        self.state_manager = self.game.state_manager
        self.output_manager = self.game.output_manager
        self.input = None
        self.stage = None
        self.inquirer = inquirer

    def prompt_list_input(self):
        questions = []
        if self.state_manager.current_state == State.MENU:
            questions.append(input_content[MenuState.MENU_LOAD]["intro_menu"])
        

        return inquirer.prompt(questions)
    

    def receive_input(self):
        return input(f"{input_dialogue}")

    def setInput(self, input, stage):
        self.input = input
        self.stage = stage

    def getInput(self):
        return self.input
    
    def getStage(self):
        return self.stage

    def start_new_game(self):
        self.state_manager.current_sub_state = MenuState.MENU_NEW_GAME
        isComplete = self.output_manager.output_start_game_dialogue()
        if isComplete:
            self.output_manager.output_start_game_lore()

    def about_game(self):
        self.state_manager.current_sub_state = MenuState.MENU_ABOUT
        self.output_manager.output_about_menu_lore()

    def load_game(self):
        self.state_manager.current_sub_state = MenuState.MENU_LOAD_GAME
        self.output_manager.output_load_game_dialogue()

    def quit_game(self):
        self.state_manager.current_sub_state = MenuState.MENU_QUIT_GAME
        self.output_manager.output_quit_game_dialogue()
        quit()