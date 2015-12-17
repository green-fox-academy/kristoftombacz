import os
import json
import menus
from menu import Menu

from random import randint
from character import Player
from store import StoreName

player1 = Player('', 0, 0, 0)
return_menu_name = StoreName()

def username_input():
	user_input = input('\nPlease write your name: ')
	player1.name = user_input
	
	return user_input

def username_print(username):
	user_input_text = '\nYour username is: ' + username
	print(user_input_text)

def new_game():
	os.system('clear')
	username_print(username_input())
	new_game_submenu = Menu(menus.second_menu)
	return_menu_name.get_name(menus.second_menu)
	new_game_submenu.menu_summary()

def resume():
	os.system('clear')
	new_game_submenu = Menu(return_menu_name.return_name())
	prev_menu_name = new_game_submenu.get_menu_name()
	prev_menu = Menu(prev_menu_name)
	prev_menu.menu_summary()

def quit():
	os.system('clear')
	quit_submenu = Menu(menus.third_menu)
	quit_submenu.menu_summary()

def save_and_quit():
	os.system('clear')
	filename = open('save.json', 'w')
	json.dump(player1.create_dictionary(), filename)
	filename.close()
	exit()

def save():
	filename = open('save.json', 'w')
	json.dump(player1.create_dictionary(), filename)
	filename.close()
	return_menu = Menu(return_menu_name.return_name())
	return_menu.menu_summary()

def random_cube():
	rnd = randint(1,6)
	return rnd

def random_cube_double():
	rnd = randint(1,6) + randint(1,6)
	return rnd

def roll_stats():
	os.system('clear')
	
	player1.dexterity = random_cube() + 6
	player1.health = random_cube_double() + 12
	player1.luck = random_cube() + 6
	player1.max_health = player1.health
	player1.max_luck = player1.luck
	
	print(
		"\nHealth: " + str(player1.health) + 
		" | Dexterity: " + str(player1.dexterity) + 
		" | Luck: "  + str(player1.luck)
	)

def contineu():
	os.system('clear')
	roll_stats()
	continue_submenu = Menu(menus.fourth_menu)
	return_menu_name.get_name(menus.fourth_menu)
	continue_submenu.menu_summary()

def potion():
	os.system('clear')
	potion_submenu = Menu(menus.fifth_menu)
	return_menu_name.get_name(menus.fifth_menu)
	print('\n Choose one potion from below!')
	potion_submenu.menu_print()

	input_number = potion_submenu.menu_input()
	potion_name = potion_submenu.get_item_name(input_number)
	player1.add_inventory(potion_name)

	potion_submenu.menu_selector(input_number)
	
def potion_selector():
	os.system('clear')

	if 'Potion of' in player1.inventory[2]:
		print('\nYou chose: ' + player1.inventory[2])

	potion_selector_submenu = Menu(menus.sixth_menu)
	return_menu_name.get_name(menus.sixth_menu)
	potion_selector_submenu.menu_summary()

def character():
	os.system('clear')
	print(player1.character_table())
	begin_game_menu = Menu(menus.seventh_menu)
	return_menu_name.get_name(menus.seventh_menu)
	begin_game_menu.menu_summary()
