from src.constants.states import State, PuzzleState, MenuState

menu_styles = {
    MenuState.MENU_LOAD: [
        "bold white on black", 
        "bold white on black"
        ],
    MenuState.MENU_ABOUT: [
        "bold white on black",
        "bold white on black",
        "bold white on black",
        "bold white on black",
        "bold white on black"
    ],
    MenuState.MENU_NEW_GAME: [
        "bold white on black",
    ],
    MenuState.MENU_LOAD_GAME: [
        "Reactivating previous mission... restoring your drone fleet.",
        "Retrieving last expedition logs... recalibrating for the next dive.",
        "Re-engaging the ship's systems... continuing your legacy.",
        "Reactivating old data... new ruins detected nearby.",
        "Syncing with last successful dive... ready to push deeper.",
    ]
}