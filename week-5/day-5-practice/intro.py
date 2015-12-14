names = [
	{'id': 1, 'name': 'John'},
	{'id': 2, 'name': 'Molly'},
	{'id': 3, 'name': 'Jane'}
	]

class MyMagic:
	def __init__(self, list_of):
		self.database = list_of

	def names_as_list(self):
		return list(map(lambda u: u['name'], self.database))

	def names_start_with_j(self):
		return list(filter(lambda name: name.startswith('J'), self.names_as_list()))

mm = MyMagic(names)
