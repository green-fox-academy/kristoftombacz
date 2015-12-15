import unittest
from menu import Menu

test_build = '''
_________________________

     1 - valami
     2 - valami2
     3 - valami3
_________________________'''

class TestMenu(unittest.TestCase):
	def test_class_exist(self):
		new_class = Menu(('Jaj', 'Jaj2'))
	
	def test_menu_print(self):
		test_menu = (
				{'name': 'valami', 'id': 1},
				{'name': 'valami2', 'id': 2},
				{'name': 'valami3', 'id': 3}
			)
		new_class = Menu(test_menu)
		self.assertEqual(test_build, new_class.menu_print())

	def test_tuple(self):
		test_menu = ('Elso', 'Masodik', 'Harmadik')
		new_class = Menu(test_menu)
		self.assertEqual(test_menu[1], 'Masodik')
		
#	def test_selector(self):
		

unittest.main()
