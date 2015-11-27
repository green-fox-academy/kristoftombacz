from random import randint


def get_integer():
	number = int(input("Enter an integer: "))
	return number
	
numbertoguess = randint(0, 10)	
numberguesses = 5


def check(rightnumber, guess, numberguesses):
	if rightnumber == guess:
		print("Eltalaltad")
		numberguesses = 0

	elif rightnumber > guess:
		print("Tul kicsi a szamod")
	else:
		print("Tul nagy a szamod")
	return numberguesses

while numberguesses > 0:
	try:
		number = get_integer()
		numberguesses = check(numbertoguess, number, numberguesses)
		numberguesses -= 1
		print(numberguesses)

	except ValueError:
		print("Wrong values mate!")

