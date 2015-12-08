import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
	def test_existence(self):
		wizard = Wizard('Harry Potter az otodik konyvben', 50, 50, 20)
	
	def test_inheritance(self):
		wizard = Wizard('Harry Pooota', 50, 50, 20)
		self.assertEqual(wizard.hp, 50)
	
	def test_manna(self):
		wizard = Wizard('Harrrryyyy', 50, 50, 20)
		self.assertEqual(wizard.manna, 20)
	
	def test_strike(self):
		wizard = Wizard('HARYYRYR', 50, 50, 20)
		opponent = Wizard('Tom Denem', 100, 70, 20)
		wizard.strike(opponent)
		self.assertEqual(opponent.hp, -50)

	def test_strike_wo_mana(self):
		wizard = Wizard('GHAARRiYYY', 50, 30, 0)
		opponent = Wizard('VOLDERMORT', 100, 70, 20)
		wizard.strike(opponent)
		self.assertEqual(opponent.hp, 90)

	def test_manna(self):
		wizard = Wizard('hafaprotter', 50, 50, 20)
		opponent = Wizard('VODLMER', 100, 70, 20)
		wizard.strike(opponent)
		self.assertEqual(wizard.manna, 15)

unittest.main()	
