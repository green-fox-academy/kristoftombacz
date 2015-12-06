import json
import menu

def create():
	user_input = input('\n' + 'Choose a name for your to-do list: ')
	print('')
	filename = open(user_input + '.json', 'w')

def load():
	loaded = []
	filename = open(menu.getHu(), 'r')

	try:
		loaded = json.load(filename)
	except Exception:
		pass
	filename.close()

	return loaded

def save(list):
	filename = open(menu.getHu(), 'w')
	json.dump(list, filename)
	filename.close()
