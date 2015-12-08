import unittest
from decorator import TrashCan

class RustyTest(unittest.TestCase):
	def test_rusty_effect(self):
		weapon = TrashCan()
		self.assertEqual(5, weapon.damage())

unittest.main()
