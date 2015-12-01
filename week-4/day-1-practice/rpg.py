class Player:
	def __init__(self, name, damage, hp = 100):
		self.name = name
		self.hp = hp
		self.damage = damage
	
	def print_status(self):
		if self.hp <= 0:
			print(self.name, 'is dead!')
		else:
			print('He is', self.name, 'and his hp', self.hp)

	def drink_potion(self):
		if self.hp >= 90:
			self.hp = 100
		elif self.hp <= 0:
			print('A dead person can\'t drink a potion :(')
		else:
			self.hp += 10
		self.print_status()
	
	def strike(self, towho):
		towho.hp -= self.damage
		if towho.hp < 0:
			towho.hp = 0
		print(self.name, 'strikes', towho.name, 'with a big tuna! Damaged', self.damage, 'hp!')

class Cerlic(Player):
	def heal(self, ally):
		ally.hp += 10
		print(self.name, 'healed', ally.name, 'with 10 hp')

gyuri = Player('gyuri', 50)
taho = Player('taho', 10)
melkor = Cerlic('Melkor', 1000, 80)

gyuri.print_status()
taho.print_status()

for i in range(4):
	melkor.heal(taho)
	gyuri.strike(taho)

taho.print_status()
taho.drink_potion()
