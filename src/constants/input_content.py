import inquirer
from src.constants.states import State, PuzzleState, MenuState

input_content = {
    MenuState.MENU_LOAD: {
        "intro_menu": inquirer.List('menu',
                message="Main Menu (Select An Option)",
                choices=['Start New Game', 'Load Game', 'About Game', 'Quit Game'],
            )
    }
}