class Character:
	
	def __init__(self, name, health, dexterity):
		self.name = name
		self.max_health = health
		self.health = health
		self.dexterity = dexterity

	def change_status(self, status, amount, operator):
		if operator == '+':		
			self.status += amount
		elif operator == '-':
			self.status -= amount
		else:
			print('Wrong operator input')
	
	def character_table(self):
		character = ''
		character += '\nName: ' + str(self.name) + ' | Health: ' + str(self.health) + ' | Dexterity: ' + str(self.dexterity) + ' | Luck: ' + str(self.luck)
		character += '\nInventory: '
		for n in self.inventory:
			character += n + ' | '
	
		return character
	def fight_menu(self):
		fight_menu = ''
		fight_menu += '\nName: ' + str(self.name) + '\n'
		fight_menu += 'Max Health: ' + str(self.max_health) + ' | Current Health: ' + str(self.health) + '\n'
		fight_menu += 'Dexterity: ' + str(self.dexterity) + '\n'
		fight_menu += 'Max Luck: ' + str(self.max_luck) + ' | Current Luck: ' + str(self.luck) + '\n'

		return fight_menu
	
class Player(Character):
	def __init__(self, luck):
		super().__init__()
		self.max_luck = luck
		self.luck = luck
		self.inventory = ['Sword', 'Leather Armor', '']
	
	def add_inventory(self, item):
		self.inventory[2] = item
	
	def create_dictionary(self):
		dictionary = {'name': self.name, 'health': self.health, 'dexterity': self.dexterity, 'luck': self.luck, 'inventory': self.inventory}

		return dictionary

class Monster():
	pass

