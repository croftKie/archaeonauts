# PUZZLE DATA STRUCTURE

"""
Puzzle:
    id: int
    type: string
    race: string
    lore: string
    steps:
        {
            step_id: int
            step_lore: string
            step_answer: string | int
            step_is_complete: bool
            clues:
                {
                clue_triggers: string[]
                clue_text: string[]
                }[]
        }[]
"""


