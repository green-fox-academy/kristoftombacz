class Car:
	def __init__ (self, color, type, km):
		self.color = color
		self.type = type
		self.km = km

	def ride(self, km):
		self.km += km

	def getMiles(self):
		return self.km * 0.6213


tesla = Car('pink', 'Tesla S', 1200)

tesla.ride(220)
tesla.ride(100)

print(tesla.getMiles())
print(tesla.km)
