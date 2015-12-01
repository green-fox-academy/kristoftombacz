numbers = [4, 5, 6, 7, 8, 9, 10]

def summ(list):
	sum = 0
	for n in list:
		sum += n
	return sum

print(summ(numbers))
print(summ([1,2,3]))
