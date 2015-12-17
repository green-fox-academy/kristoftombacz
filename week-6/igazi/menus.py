from commands import *
from fight import *
from store import *

first_menu = (
		{'number':1, 'name': 'New Game', 'function': new_game},
		{'number':2, 'name': 'Load Game', 'function': load_game},
		{'number':3, 'name': 'Exit', 'function': exit}
	)

second_menu = (
		{'number': 1, 'name': 'Reenter name', 'function': new_game},
		{'number': 2, 'name': 'Continue', 'function': contineu},
		{'number': 3, 'name': 'Save', 'function': save},
		{'number': 4, 'name': 'Quit', 'function': quit}
	)

third_menu = (
		{'number': 1, 'name': 'Save and Quit', 'function': save_and_quit},
		{'number': 2, 'name': 'Quit without save', 'function': exit},
		{'number': 3, 'name': 'Resume', 'function': resume}
	)

fourth_menu = (
		{'number': 1, 'name': 'Reroll stats', 'function': contineu},
		{'number': 2, 'name': 'Continue', 'function': potion},
		{'number': 3, 'name': 'Save', 'function': save},
		{'number': 4, 'name': 'Quit', 'function': quit}
	)

fifth_menu = (
		{'number': 1, 'name': 'Potion of Health', 'function': potion_selector},
		{'number': 2, 'name': 'Potion of Dexterity', 'function': potion_selector},
		{'number': 3, 'name': 'Potion of Luck', 'function': potion_selector}
	)

sixth_menu = (
		{'number': 1, 'name': 'Reselect the Potion', 'function': potion},
		{'number': 2, 'name': 'Continue', 'function': character},
		{'number': 3, 'name': 'Quit', 'function': quit}
	)

seventh_menu = (
		{'number': 1, 'name': 'Begin', 'function': begin},
		{'number': 2, 'name': 'Save', 'function': save},
		{'number': 3, 'name': 'Quit', 'function': quit}
	)		

eighth_menu = (
		{'number': 1, 'name': 'Add new item', 'function': add_new_item},
		{'number': 2, 'name': 'Resume', 'function': resume},
		{'number': 3, 'name': 'Quit', 'function': quit}
	)		

begin_menu = (
		{'number': 1, 'name': 'Strike', 'function': strike},
		{'number': 2, 'name': 'Retreat', 'function': None},
		{'number': 3, 'name': 'Quit', 'function': quit}
	)
strike_submenu = (
		{'number': 1, 'name': 'Continue', 'function': begin},
		{'number': 2, 'name': 'Try your luck', 'function': try_your_luck},
		{'number': 3, 'name': 'Retreat', 'function': None},
		{'number': 4, 'name': 'Quit', 'function': exit}
	)
