from src.constants.states import MenuState, PuzzleState, State

class StateManager():
    def __init__(self, game):
        self.game = game
        self.current_state = State.MENU
        self.current_sub_state = MenuState.MENU_LOAD

    def get_current_state(self):
        return self.current_state
    def get_current_sub_state(self):
        return self.current_sub_state

