import json

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
