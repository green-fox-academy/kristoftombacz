import store
import commands

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

while True:
    menu()
