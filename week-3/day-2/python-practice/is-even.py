def is_even(number):
	if number % 2 == 0:
		print(str(number) + " páros!")
	else:
		print(str(number) + " páratlan")

temp = input("adj meg egy szamot: ")
number = int(temp)

is_even(number)
