import os

class StoreName:
	def __init__(self, name = None):
		self.name = name

	def get_name(self, menu_name):
		self.name = menu_name	

	def return_name(self):
		return self.name

def list_json():
	json = []
	for file in os.lisdir():
		if file.endswith('*.json'):
			json.append(file)
	return json
