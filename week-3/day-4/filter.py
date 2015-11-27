numbers = [1,2,3,4,5,6,7,8]
output = []

def even(numb_list):
	for i in numb_list:
		if i % 2 == 0:
			output.append(i)
	print(output)

even(numbers)

