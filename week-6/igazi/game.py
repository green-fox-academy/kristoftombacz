import json
from menu import Menu
from random import randint
from character import Character

player1 = Character('', 0, 0, 0)

def username_input():
	user_input = input('\nPlease write your name: ')
	player1.name = user_input
	
	return user_input

def username_print(username):
	user_input_text = '\nYour username is: ' + username
	print(user_input_text)

def new_game():
	username_print(username_input())
	new_game_submenu = Menu(second_menu)
	new_game_submenu.menu_summary()

def resume():
	new_game_submenu = Menu(second_menu)
	new_game_submenu.menu_summary()

def quit():
	quit_submenu = Menu(third_menu)
	quit_submenu.menu_summary()

def save():
	filename = open('save.json', 'w')
	json.dump(character, filename)
	filename.close()
	exit()

def random_cube():
	rnd = randint(1,6)
	return rnd

def roll_stats():
	
	player1.dexterity = random_cube() + 6
	player1.health = random_cube() + random_cube() + 12
	player1.luck = random_cube() + 6
	
	print("Health: " + str(player1.health) + " | Dexterity: " + str(player1.dexterity) + " | Luck: "  + str(player1.luck))

def contineu():
	roll_stats()
	continue_submenu = Menu(fourth_menu)
	continue_submenu.menu_summary()

def potion():
	potion_submenu = Menu(fifth_menu)
	potion_submenu.menu_print()

	input_number = potion_submenu.menu_input()
	potion_name = potion_submenu.get_item_name(input_number)
	
	print('\nYou choose: ' + potion_name)
	player1.add_inventory(potion_name)

	potion_submenu.menu_selector(input_number)
	
def potion_selector():
	potion_selector_submenu = Menu(sixth_menu)
	potion_selector_submenu.menu_summary()

def character():
	print(player1.character_table())
	begin_game_menu = Menu(seventh_menu)
	begin_game_menu.menu_summary()

first_menu = (
		{'number':1, 'name': 'New Game', 'function': new_game},
		{'number':2, 'name': 'Load Game', 'function': None},
		{'number':3, 'name': 'Exit', 'function': exit}
	)

second_menu = (
		{'number': 1, 'name': 'Reenter name', 'function': new_game},
		{'number': 2, 'name': 'Continue', 'function': contineu},
		{'number': 3, 'name': 'Save', 'function': None},
		{'number': 4, 'name': 'Quit', 'function': quit}
	)

third_menu = (
		{'number': 1, 'name': 'Save and Quit', 'function': save},
		{'number': 2, 'name': 'Quit without save', 'function': exit},
		{'number': 3, 'name': 'Resume', 'function': resume}
	)

fourth_menu = (
		{'number': 1, 'name': 'Reroll stats', 'function': contineu},
		{'number': 2, 'name': 'Continue', 'function': potion},
		{'number': 3, 'name': 'Save', 'function': None},
		{'number': 4, 'name': 'Quit', 'function': None}
	)

fifth_menu = (
		{'number': 1, 'name': 'Potion of Health', 'function': potion_selector},
		{'number': 2, 'name': 'Potion of Dexterity', 'function': potion_selector},
		{'number': 3, 'name': 'Potion of Luck', 'function': potion_selector}
	)

sixth_menu = (
		{'number': 1, 'name': 'Reselect the Potion', 'function': potion},
		{'number': 2, 'name': 'Continue', 'function': character},
		{'number': 3, 'name': 'Quit', 'function': None}
	)

seventh_menu = (
		{'number': 1, 'name': 'Begin', 'function': None},
		{'number': 2, 'name': 'Save', 'function': None},
		{'number': 3, 'name': 'Quit', 'function': exit}
	)		
	
main_menu = Menu(first_menu)
main_menu.menu_summary()
