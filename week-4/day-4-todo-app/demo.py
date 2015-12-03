import json

students = [

	{'description': 'vegyel tejet', 'status': 'done'},
	{'description': 'vegyel mosoport', 'status': 'todo'},
	{'description': 'vegyel kascat', 'status': 'todo'}
]

def menu_print():
	
	print('\033[46m', '********************************************************')		
	print(' *                                                      *')
	print(' *         1   List items                               *')
	print(' *         2   Add items                                *')
	print(' *         3   Complete items                           *')
	print(' *         4   Remove items                             *')
	print(' *         5   Exit from the program                    *')
	print(' *                                                      *')
	print(' ********************************************************')
	

def menu():
	try:
		while True:
			menu_print()
			user_input = input('Please choose: ')
			if int(user_input) == 1:
				lists(load())
			
			elif int(user_input) == 2:
				add(load())
				lists(load())
			
			elif int(user_input) == 3:
				lists(load())
				complete(load())
			
			elif int(user_input) == 4:
				lists(load())
				remove(load())
			
			elif int(user_input) == 5:
				break
			else:
				print('Wront input!')
			
	except ValueError:
		print('')
		print('Please only enter numbsers!')
		print('')
		menu()

def main():
	menu()

def load():
	loaded = []
	filename = open('load.json', 'r')
	
	try:
		loaded = json.load(filename)
	except Exception:
		pass

	filename.close()
	return loaded

def save(list):
	filename = open('load.json', 'w')
	json.dump(list, filename)

	filename.close()
def lists(list):
	i = 1
	for n in list:
		print(i, n['description'], n['status'])
		i += 1

def add(list):
	user_input = input('\nPlease enter the description: ')
	list.append({'description': user_input, 'status': 'todo'})
	save(list)

def complete(list):
	user_input = input('\nPlease enter the number to complete: ')
	
	n = int(user_input) - 1 
	list[n]['status'] = 'done'
	
	save(list)
	return list

def remove(list):
	user_input = input('\nPlease enter thenumber to remove: ')
	
	n = int(user_input) - 1
	list.pop(n)
	
	save(list)
	return list

main()
#lists(students)
#add(students)
#lists(students)
#lists(remove(students))
