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
        self.isPlaying = False
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

        while not self.isPlaying:
            answer = self.input_manager.prompt_list_input()
            if answer["menu"] == "Start New Game":
                self.__start_new_game()
                self.isPlaying = True

            if answer["menu"] == "About Game":
                self.__about_game()
            
            if answer["menu"] == "Load Game":
                self.__load_game()
            
            if answer["menu"] == "Quit Game":
                self.__quit_game()

        while self.isPlaying:


            latest_input = self.input_manager.receive_input()
            return
    
    def __update(self):
        return
    
    ## Utilities

    def __start_new_game(self):
        self.current_sub_state = MenuState.MENU_NEW_GAME
        isComplete = self.output_manager.output_start_game_dialogue()
        if isComplete:
            self.output_manager.output_start_game_lore()

    def __about_game(self):
        self.current_sub_state = MenuState.MENU_ABOUT
        self.output_manager.output_about_menu_lore()

    def __load_game(self):
        self.current_sub_state = MenuState.MENU_LOAD_GAME
        self.output_manager.output_load_game_dialogue()

    def __quit_game(self):
        self.current_sub_state = MenuState.MENU_QUIT_GAME
        self.output_manager.output_quit_game_dialogue()
        quit()