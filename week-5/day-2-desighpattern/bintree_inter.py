class Node:
	def __init__(self, value, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

root = Node(1, Node(2), Node(3))

class LeftIterator:
	def __init__(self, root):
		self.curr = root

	def next(self):
		return self.curr is not None

	def current(self):
		temp = self.curr
		self.curr = self.curr.left
		return temp

iter = LeftIterator(root)
while iter.next():
	print(iter.current().value)
