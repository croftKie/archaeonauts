from src.constants.states import State, PuzzleState, MenuState

input_dialogue = "ArcheoTerminal:: "

menu_dialogue = {
    MenuState.MENU_LOAD: [
        "Welcome to Archeonauts!", 
        "Prepare yourself, Exo-Archeologist. The ruins await.",
        ],
    MenuState.MENU_ABOUT: [
        "The year is 2134. Humanity has reached out into the stars, unlocking the mysteries of the solar system—once filled with only human hope—now teeming with the echoes of long-forgotten civilizations.",
        "As an exo-archeologist, your job is to delve into the ruins of these alien societies, uncovering ancient knowledge and forgotten technology. Armed with only your wits and a fleet of drones, you will explore the remnants of alien cities, decipher cryptic puzzles, and unearth the secrets buried deep within.",
        "But be warned. The path ahead is fraught with dangers. Your drones are your lifeline, and the ruins can be treacherous. Lose them, and you will have to retreat, your progress lost until the next expedition. But success brings reward. Fame. Wealth. Infamy. These are the currencies that will determine your standing in the Solar System.",
        "You are not alone in this. The Coalition of peaceful nations stands with you—Old Europe, the Americas, Africanus, and Nihon/Hanguk—united in the pursuit of knowledge. Yet, there are those who still cling to the old ways, living outside the Coalition’s reach: the United Free States and the SinoRus Alliance. The old conflicts may be over, but some wounds never heal.",
        "Your journey will define not just your future, but the future of humanity. As you uncover the lost history of the ancient civilizations that once inhabited our solar system, remember: you are both a student of history and a creator of it."
    ],
    MenuState.MENU_NEW_GAME: [
        "Initializing new profile... beginning your journey into the stars.",
        "Launching first expedition... setting coordinates for the unknown.",
        "New mission accepted... drones are ready for deployment.",
        "Starting from scratch... preparing to uncover humanity's ancient past.",
        "Configuring your equipment... the ruins await your discovery.",
    ],
    MenuState.MENU_LOAD_GAME: [
        "Reactivating previous mission... restoring your drone fleet.",
        "Retrieving last expedition logs... recalibrating for the next dive.",
        "Re-engaging the ship's systems... continuing your legacy.",
        "Reactivating old data... new ruins detected nearby.",
        "Syncing with last successful dive... ready to push deeper.",
    ]
}