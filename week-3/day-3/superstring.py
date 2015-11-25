class MySuperString:
	def __init__(self, mystring):
		self.mystring = mystring

	def reverse(self):
		stringlen = len(self.mystring)
		reversed = ''

		for i in range(stringlen):
			reversed = self.mystring[i] + reversed
		return reversed

	def count(self, char):
		stringlen = len(self.mystring)
		count = 0
		
		for i in range(stringlen):
			if self.mystring[i] == char:
				count += 1
			

		return count

	def nospace(self):
		newstring = ''
				
		for i in self.mystring:
			if i == ' ':
				newstring = newstring + '_'
			else:
				newstring = newstring + i

		return newstring

class MyMath:
	
	def __init__(self,num_list):
		self.num_list = num_list

	def average(self):
		sum = 0
		count = 0
		
		for i in self.num_list:
			sum += i
			count += 1

		return sum/count



