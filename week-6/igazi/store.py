class StoreName:
	def __init__(self, name = None):
		self.name = name

	def get_name(self, menu_name):
		self.name = menu_name	

	def return_name(self):
		return self.name
