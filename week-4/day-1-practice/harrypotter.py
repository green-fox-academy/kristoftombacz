temp = input('How many first book you want to order MATEE? ')
first = int(temp)
temp = input('How many from the second book: ')
second = int(temp)
temp = input('How many from the third: ')
third = int(temp)
temp = input('How many from the fourth: ')
fourth = int(temp)
temp = input('How many from the fifth: ')
fifth = int(temp)


def discount():
	disc = 5
	sum = 0
	sum = (first*8) + (second*8) + (third*8) + (fourth*8) + (fifth*8)
	
	return sum
	

print(discount())
