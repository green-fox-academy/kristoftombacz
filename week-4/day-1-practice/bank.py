class Bank_account:
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
	
	def pay(self, amount):
		self.balance -= amount

	def receive(self, amount):
		self.balance += amount

	def print_balance(self):
		print('Balance of |', self.name, '| is |', self.balance, '$|')

	def swap(self, amount, towho):
		towho.receive(amount)
		self.pay(amount)


kacsa = Bank_account('kacsa laci', 25)
aranyhal = Bank_account('aranyhal tomi', 99999)

kacsa.pay(100)
kacsa.receive(10)
aranyhal.swap(5000, kacsa)

kacsa.print_balance()
aranyhal.print_balance()
