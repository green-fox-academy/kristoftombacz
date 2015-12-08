class Warrior:
	def __init__(self):
		self.companions = []
		self.hp = 100

	def join(self, companion):
		self.companions.append(companion)
	
	def strike(self, opponent):
		opponent.inflict_damage(10)

	def inflict_damage(self, damage):
		self.hp -= damage
		for companion in self.companions:
			companion.notify('damage', self)

	def _notify_all(self, type):
		for companion in self.companions:
			companion.notify(type, self)

	def heal(self, hp):
		self.hp += hp

	def curse(self, opponent):
		opponent.join(Curse())
		self._notify_all('curse')

class BattleField:

	def __init__(self):
		warriors = []
		self.warriors = warriors

	def notify(self, type, warrior):
		if type == "damage" or type == "curse":
			warrior.heal(-20)

	def join(self, warrior):
		self.warriors.append(warriors)

class Healer:

	def __init__(self):
		self.companions = []
		self.hp = 100

	def notify(self, type, warrior):
		if type == "damage":
			warrior.heal(5)

	def join(self, companion):
		self.companions.append(companion)

class Curse:

	def __init__(self):
		self.companions = []
		self.hp = 100

	def notify(self, type, warrior):
		if type == "damage":
			warrior.heal(-30)

	def join(self, companion):
		self.companions.append(companion)

class Cheer:

	def __init__(self):
		self.companions = []
		self.hp = 100

	def notify(self, type, warrior):
		if type == "curse":
			print("Hurray!!")


	def join(self, companion):
		self.companions.append(companion)

rabbit = Warrior()
wolf = Warrior()
shaman = Healer()

rabbit.join(BattleField())
wolf.join(BattleField())

rabbit.join(shaman)
wolf.join(Cheer())

wolf.curse(rabbit)
wolf.strike(rabbit)

print("Rabbit hp: " + str(rabbit.hp))
print("Wolf hp: " + str(wolf.hp))
