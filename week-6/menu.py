class Menu:
	def __init__(self, tuple_menu):
		self.tuple_menu = tuple_menu
	
	def menu_print(self):
		menu = ''
		menu += ("\n" + "_"*25 + "\n\n")
		
		for n in self.tuple_menu:
			menu += (" "*5 + str(n['id']) + " - " + n['name'] + "\n")
		
		menu += ("_"*25)
		
		return menu
		
	def menu_input(self):
		while True:
			try:
				input_int = int(input("\nPlease choose from the menu: "))
				break
			except ValueError:
				print("\n Wrong Input")
		
		return input_int

	def menu_selector(self):
		while True:
			print(self.menu_print())
			input_int = self.menu_input()

			if input_int < len(self.tuple_menu):
				for n in self.tuple_menu:
					if input_int == n['id']:
						n['function']()
			
			elif input_int == len(self.tuple_menu):
				user_input = input('Are you really want to exit (y/n)? ')
				
				if user_input.lower() == 'y':
					exit()
				elif user_input.lower() == 'n':
					pass
				else:
					print('\nWrong input')
			else:
				print("Please choose from the menu: ")

