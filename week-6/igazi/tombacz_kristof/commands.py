import os
import json
import menus
from menu import Menu

from random import randint
from character import Player
from store import StoreName
from fight import *

player1 = Player('lala', 0, 0, 0)
return_menu_name = StoreName()

def username_input():
	user_input = input('\nPlease write a name for your character: ')
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

def roll_stats_print():
	print(
		"\nHealth: " + str(player1.health) + 
		" | Dexterity: " + str(player1.dexterity) + 
		" | Luck: "  + str(player1.luck)
	)

def contineu():
	os.system('clear')
	roll_stats()
	roll_stats_print()
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

def list_json():
	json = []
	for file in os.listdir():
		if file.endswith('.json'):
			json.append(file)
	return json

def save_and_quit():
	save()
	exit()

def save_character():
	filename = open('save.json', 'w')
	json.dump(player1.create_dictionary(), filename)
	filename.close()
	return_menu = Menu(return_menu_name.return_name())
	return_menu.menu_summary()

def save():
	os.system('clear')
	print('\n')
	for files in list_json():
		print(' '*5 + files)
	save_submenu = Menu(menus.eighth_menu)
	save_submenu.menu_summary()

def add_new_item():
	filename_input = input('\nPlease write a filename: ')
	filename = open(filename_input + '.json', 'w')
	json.dump(player1.create_dictionary(), filename)
	filename.close()

	save()

def load_game():
	os.system('clear')
	print('\n')
	i = 1
	for files in list_json():
		print(' '*5 + str(i) + ' - ' + files)
		i += 1

	load_game = Menu(list_json())
	loaded = load_game.menu_input()

	i = 1
	for item in list_json():
		if i == loaded:
			filename = open(item, 'r')
			loading = json.load(filename)

			player1.name = loading['name']
			player1.health = loading['health']
			player1.max_health = loading['health']
			player1.dexterity = loading['dexterity']
			player1.luck = loading['luck']
			player1.max_luck = loading['luck']
			player1.inventory = loading['inventory']
			filename.close()
		i += 1
	begin(player1)
def add_at():
	valami = player1
	return valami

def retreat():
	print('\nYou have to buy the DLC to retreat, sorry :c')
	print('Only 100$, but because of christmas you can get it for 30$ 30$, THIRTYYYY $$$$$$!\n')
	input('Press a key to continue...')
	begin(player1)

