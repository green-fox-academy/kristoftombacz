class Character:
	
	def __init__(self, name, health, dexterity, luck):
		self.name = name
		self.health = health
		self.dexterity = dexterity
		self.luck = luck
		self.inventory = ['Sword', 'Leather Armor', '']
	
	def add_inventory(self, item):
		self.inventory[2] = item
	
	def character_table(self):
		character = ''
		character += '\nName: ' + str(self.name) + ' | Health: ' + str(self.health) + ' | Dexterity: ' + str(self.dexterity) + ' | Luck: ' + str(self.luck)
		character += '\nInventory: '
		for n in self.inventory:
			character += n + ' | '
	
		return character
