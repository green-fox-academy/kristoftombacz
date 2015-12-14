def adder(array):
	add = lambda x : x+1
	return list(map(add, array))

def filterArray(array):	
	return list(filter(lambda x : x % 3 == 0, array))
