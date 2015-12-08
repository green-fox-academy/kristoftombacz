import unittest
from counter import count_letters

class LetterCounterTest(unittest.TestCase):
	def test_if_exists(self):
		self.assertEqual(count_letters(''), {})
	
	def test_simple_letters(self):
		self.assertEqual(count_letters('a'), {'a': 1})
		self.assertEqual(count_letters('b'), {'b': 1})
	
	def test_multiple_letters(self):
		self.assertEqual(count_letters('aa'), {'a': 2})
		self.assertEqual(count_letters('ab'), {'a': 1, 'b': 1})

	def test_multiple_diff_letter(self):
		self.assertEqual(count_letters('aabasd'), {'a': 3, 'b': 1, 'd': 1, 's': 1})
		self.assertEqual(count_letters('aaaaaabbassddf'), {'a': 7, 'b': 2, 'd': 2, 's': 2, 'f': 1})

unittest.main()
