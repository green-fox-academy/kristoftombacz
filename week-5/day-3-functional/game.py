
class Character():

	def __init__(self, hp = 20, armor = 10):
		self._hp = hp
		self._armor = armor
		self._isAlive = True
	
	def sufferDamage(self, damage):
		sufferedDamage = self._hp + self._armor - damage

		if sufferedDamage < 1:
			self._isAlive = False

	def heal(self, heal):
		self._hp += heal
			
	def isAlive(self):
		return self._isAlive

	def getHealth(self):
		return self._hp

def handleEvents(events):
	list(map(handleEvent, events))

def handleEvent(event):
	eventHandlers[event['type']](event)

def applyHeal(event):
	event['character'].heal(event['size'])
	
def applyDamage(event):
	event['character'].sufferDamage(event['size'])

eventHandlers = {
	'damage': applyDamage,
	'heal': applyHeal
}
