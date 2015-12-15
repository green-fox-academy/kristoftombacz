from menu import Menu
import commands

first_menu = (
		{'name': 'New game', 'function': commands.new_game_commands, 'id': 1},
		{'name': 'Load game', 'function': None , 'id': 2},
		{'name': 'Exit', 'function': None , 'id': 3}
	)

first = Menu(first_menu)
first.menu_selector()
