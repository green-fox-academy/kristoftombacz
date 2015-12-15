
class Menu:

	def __init__(self, items):
		self.items = items

	def menu_input(self):
		while True:
			try:
				input_int = int(input("\nPlease choose from the menu: "))
				break
			except ValueError:
				print("\n Wrong Input")

		return input_int

	def return_last_input(self):
		return last_input

	def menu_print(self):
		menu = ''
		menu += ("\n" + "_"*25 + "\n\n")
		
		for n in self.items:
			menu += (" "*5 + str(n['number']) + " - " + n['name'] + "\n")
		
		menu += ("_"*25)
		
		print(menu)
	
	def menu_selector(self, number):
		for item in self.items:
			if item['number'] == number:
				return item['function']()
		
	def menu_summary(self):
		self.menu_print()
		self.menu_selector(self.menu_input())
