class Weapon:
	def strike(self, warrior, opponent):
		opponent.hp -= self.damage()
		warrior.hp -= self.self_damage()

	def damage(self):
		pass
	
	def self_damage(self):
		pass

class Sword(Weapon):
	def damage(self):
		return 15
	
	def self_damage(self):
		return 5

class Mace(Weapon):
	def damage(self):
		return 25

	def self_damage(self):
		return 5

class Enchanted(Weapon):
	def __init__(self, weapon):
		self.weapon = weapon

	def damage(self):
		return self.weapon.damage() * 2
	
	def self_damage(self):
		return self.weapon.self_damage() + 10

class Warrior():
	def __init__(self, name, hp, weapon):
		self.name = name
		self.hp = hp
		self.weapon = weapon
	
	def strike(self, opponent):
		self.weapon.strike(self, opponent)
		

warrior = Warrior('VARIRO', 100, Enchanted(Sword()))
opponent = Warrior('ELLENFEL', 100, Mace())
warrior.strike(opponent)
print(opponent.hp)
print(warrior.hp)
	
