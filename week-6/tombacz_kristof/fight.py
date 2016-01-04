import menus
import os
from character import *
from store import StoreName
from menu import Menu

monster = Monster('Ryuk', 5, 10)
return_menu_name = StoreName()
player_hit = None
player_luck = None
player1 = Player('', 0, 0, 0)

def pre_fight_print(yourself, opponent):
	print(	
		'\nYour character:' + yourself.fight_menu() +
		'\nYour Opponent:' + opponent.fight_menu()
	)
	
def begin(character):
	os.system('clear')
	global player_luck
	global player1

	if player_luck is None:
		pass
	elif player_luck is True:
		print('You tried your luck and succeeded')
	elif player_luck is False:
		print('You tried your luck and failed')
	
	player_luck = None

	if player_hit is None:
		print('\nTest your Sword in a test fight!\n')
	
	pre_fight_print(character, monster)
	player1 = character
	begin_fight = Menu(menus.begin_menu)
	return_menu_name.get_name(menus.begin_menu)
	begin_fight.menu_summary()

def strike():
	os.system('clear')
	global player_hit

	while True:
		player1_dexter = menus.random_cube_double() + player1.dexterity
		monster_dexter = menus.random_cube_double() + monster.dexterity

		if player1_dexter > monster_dexter:
			print('\nYou hit the monster')
			player_hit = True
			monster.health -= 2
			break
			
		elif player1_dexter < monster_dexter:
			print('\nThe monster hit you')
			player_hit = False
			player1.health -= 2
			break

	after_fight = Menu(menus.strike_submenu)
	after_fight.menu_summary()

def try_your_luck():
	global player_luck
	if player_hit is True:
		if menus.random_cube_double() > player1.luck:
			monster.health += 1
			player_luck = False			
		else:
			monster.health -= 2
			player1.luck -= 1
			player_luck = True
	else:
		if menus.random_cube_double() > player1. luck:
			player1.health -= 1
			player_luck = False
		else:
			player1.health += 1
			player1.luck -= 1
			player_luck = True
	begin(player1)
