import unittest
from monster import Monster

class TestMonster(unittest.TestCase):
	def test_existence(self):
		monster = Monster('Godzilla', 100, 10)
	
	def test_inheritance(self):
		monster = Monster('Godzilla', 500, 50)
		self.assertEqual(monster.hp, 500)
	
	def test_strike(self):
		monster = Monster('Godzilla', 500, 50)
		opponent = Monster('Wazowski', 20, 1)
		monster.strike(opponent)
		self.assertEqual(opponent.hp, -30)
		self.assertEqual(monster.hp, 502)

unittest.main()
