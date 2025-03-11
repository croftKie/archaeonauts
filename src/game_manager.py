from src.input_manager import InputManager
from src.constants.states import MenuState, PuzzleState, State
from src.output_manager import OutputManager


class GameManager():
    def __init__(self):
        self.map_manager = None
        self.player = None
        self.data_manager = None
        self.input_manager = InputManager(self)
        self.output_manager = OutputManager(self)
        self.isPlaying = True
        self.logger = None
        self.current_state = State.MENU
        self.current_sub_state = MenuState.MENU_LOAD
        
    def get_current_state(self):
        return self.current_state

    def loop(self, logger = None):
        if logger is not None:
            print("Logging Activated")
            self.logger = logger

        self.output_manager.output_menu_dialogue()
        answer = self.input_manager.prompt_list_input()

        if answer["menu"] == "Start New Game":
            self.current_sub_state = MenuState.MENU_NEW_GAME
            isComplete = self.output_manager.output_start_game_dialogue()
            if isComplete:
                self.output_manager.output_start_game_lore()

        while self.isPlaying:





            latest_input = self.input_manager.receive_input()
            return
    
    def __update(self):
        return