import unittest
from character import Character

class TestCharacter(unittest.TestCase):
	def test_exist(self):
		character = Character('Test', 100, 10)

	def test_properties(self):
		character = Character('Test', 100, 10)
		self.assertEqual(character.hp, 100)
		self.assertEqual(character.damage, 10)
		self.assertEqual(character.name, 'Test')

	def test_drink_potion(self):
		character = Character('Test', 100, 10)
		character.drink_potion()
		self.assertEqual(character.hp, 110)
		
	def test_strike(self):
		character = Character('Test', 100, 10)
		opponent = Character('Opponent', 100, 10)
		character.strike(opponent)
		self.assertEqual(opponent.hp, 90)

	def test_get_status(self):
		self.assertEqual(self.get_status_line(0, 100), 'Test')

	def test_get_status_dead(self):
		self.assertEqual(self.get_status_line(1, 0), 'DEAD')
	
	def test_get_status_alive(self):
		self.assertEqual(self.get_status_line(1, 100), 'HP: 100')

	def get_status_line(self, line_number, initial_hp):
		character = Character('Test', initial_hp, 10)
		status = character.get_status()
		first_line = status.split('\n')[line_number]
		return first_line

unittest.main()
