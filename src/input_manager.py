from src.constants.dialogue import input_dialogue
from src.constants.states import State, MenuState
from src.constants.input_content import input_content

import inquirer
class InputManager():
    def __init__(self, gm):
        self.GM = gm
        self.input = None
        self.stage = None
        self.inquirer = inquirer

    def prompt_list_input(self):
        questions = []
        if self.GM.current_state == State.MENU:
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