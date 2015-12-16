import menus
import os
from character import *
from commands import *

monster = Monster('Ryuk', 50, 5)

def pre_fight_print(yourself, opponent):
	print(	
		'\nYour character:' + yourself.fight_menu() +
		'\nYour Opponent:' + opponent.fight_menu()
	)
	

def begin():
	os.system('clear')
	print('\nTest your Sword in a test fight!\n')
	pre_fight_print(player1, monster)

	begin_fight = Menu(menus.begin_menu)
	begin_fight.menu_summary()

def strike():
	while True:
		player1_dexter = menus.random_cube() + menus.random_cube() + player1.dexterity
		monster_dexter = menus.random_cube() + menus.random_cube() + monster.desterity

		if player1_dexter > monster_dexter:
			pass

