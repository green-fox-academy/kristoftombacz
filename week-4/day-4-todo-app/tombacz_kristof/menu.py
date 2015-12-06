import os
import store
import commands
import datetime

hu = ''

def menu_print():
	print('\033[1m' + '\033[37m' + '\033[46m' + ' ********************************************************')
	print(' *                                                      *')
	print(' *         1   List items                               *')
	print(' *         2   Add items                                *')
	print(' *         3   Complete items                           *')
	print(' *         4   Remove items                             *')
	print(' *         5   Remove all completed items               *')
	print(' *         6   Exit from the program                    *')
	print(' *                                                      *')
	print(' ********************************************************' + '\033[30m' + '\033[22m')

def menu():
	try:
		menu_print()
		user_input = input('\033[47m' + 'Please choose: ')
		if int(user_input) == 1:
			commands.lists(store.load())

		elif int(user_input) == 2:
			commands.add(store.load())
			commands.lists(store.load())

		elif int(user_input) == 3:
			commands.lists(store.load())
			commands.complete(store.load())

		elif int(user_input) == 4:
			commands.lists(store.load())
			commands.removes(store.load())

		elif int(user_input) == 5:
			commands.remove_completed(store.load())

		elif int(user_input) == 6:
			exit()
		else:
			print('\n' + '\033[31m' + 'Wrong input!\n')

	except ValueError:
		print('\n' + '\033[31m' + 'Please only enter numbers!\n')
		menu()

def load_menu_print():
	print('\033[1m' + '\033[37m' + '\033[46m' + ' ********************************************************')
	print(' *                                                      *')
	print(' *         1   Create new to-do list                    *')
	print(' *         2   Use existing to-do list                  *')
	print(' *         3   Exit from the program                    *')
	print(' *                                                      *')
	print(' ********************************************************' + '\033[30m' + '\033[22m')

def load_menu():
	try:
		load_menu_print()
		user_input = input('\n' + '\033[47m' + 'Please choose: ')
		print('')
		if int(user_input) == 1:
			store.create()
			load_menu()

		elif int(user_input) == 2:
			use_menu_print()
			use_menu()

		elif int(user_input) == 3:
			exit()
		else:
			print('\n' + '\033[31m' + 'Wrong input!\n')
			load_menu()

	except ValueError:
		print('\n' + '\033[31m' + 'Please only enter numbers!\n')
		load_menu()

def use_menu_print():
	print('\033[1m' + '\033[37m' + '\033[46m' + ' ********************************************************')
	print(' *                                                      *')

	i = 0
	for file in os.listdir():
	    if file.endswith(".json"):
	        i += 1
	        print(' *         ' + str(i) + '   ' + file + '                               *')

	print(' *         ' + str(i+1) + '   Exit from the program                    *')
	print(' *                                                      *')
	print(' ********************************************************' + '\033[30m' + '\033[22m')

	return i

def use_menu():
	global hu
	try:
		user_input_inside = input('\n' + '\033[47m' + 'Please choose: ')
		print('')
		quit_value = use_menu_print()
		int_user_input = int(user_input_inside)
		jsons = list_jsons()

		if int_user_input <= quit_value:
			print('\n' + '\033[47m' + jsons[int_user_input-1] + ' loaded!' + '\n')
			hu = jsons[int_user_input-1]
		elif int_user_input == quit_value+1:
			exit()
		elif int_user_input > quit_value:
			print('\n' + '\033[31m' + 'Wrongfdf input!\n' + '\033[30m')
			use_menu()

	except ValueError:
		print('\n' + '\033[31m' + 'Please only enter numbers!\n')
		use_menu()

def getHu():
	return hu

def list_jsons():
	jsons = []
	for file in os.listdir():
	    if file.endswith(".json"):
	        jsons.append(file)
	return jsons

load_menu()
while True:
	menu()
