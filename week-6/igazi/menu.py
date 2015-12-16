class Menu:

	def __init__(self, items):
		self.items = items
	
	def get_menu_name(self):
		return self.items

	def menu_input(self):
		while True:
			try:
				input_int = int(input("\nPlease choose from the menu: "))
				return input_int
			except ValueError:
				print("\n Wrong Input")

	def menu_print(self):
		menu = ''
		menu += ("\n" + "_"*25 + "\n\n")
		for n in self.items:
			menu += (" "*5 + str(n['number']) + " - " + n['name'] + "\n")
		menu += ("_"*25)
		print(menu)

	def menu_selector(self, number):
		item = self.menu_item_selector(number)
		return item['function']()

	def menu_item_selector(self, number):
		for item in self.items:
			if item['number'] == number:
				return item

	def get_item_name(self, number):
		return self.menu_item_selector(number)['name']

	def menu_summary(self):
		self.menu_print()
		self.menu_selector(self.menu_input())
