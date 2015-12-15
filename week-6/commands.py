from menu import Menu

submenu = (
		{'name': 'Reenter name', 'function': None, 'id': 1},
		{'name': 'Continue', 'function': None, 'id': 2},
		{'name': 'Save', 'function': None, 'id': 3},
		{'name': 'Quit', 'function': None, 'id': 4}
	)	

def new_game():
	user_input = input('\nPlease write your name: ')
	return user_input

def username_print(username):
	user_input_text = '\nYour username is: ' + username
	print(user_input_text)

def new_game_submenu():
	second = Menu(submenu)
	second.menu_selector()

def new_game_commands():
	username_print(new_game())
	new_game_submenu()

