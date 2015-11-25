temp1 = input("Mennyitol menjen tesa? ")
minimum = int(temp1)

temp2 = input("es meddig? ")
maximum = int(temp2)

temp3 = input("melyik szam legyen a fizz? (az alap 3 lesz) ")
if temp3 == "":
	fizz_numb = 3
else:
	fizz_numb = int(temp3)

temp4 = input("melyik szam legyen a buzz? (az alap 5 lesz) ")
if temp4 == "":
	buzz_numb = 5
else:
	buzz_numb = int(temp4)


def get_fizzbuzz(number):
	if number % 3 == 0:
		return "fizz"
	elif number % 5 == 0:
		return "buzz"
	else:
		return number

#def is_fizz(number):
#	return number % 3 == 0 or "3" in str(number)
#def is_buzz(number):
#	return number % 5 == 0 or "5" in str(number)

def fizzish(number, base):
	return number % base == 0 or str(base) in str(number)


def fizz_buzz2(minimum, maximum):
	n = minimum
	while n <= maximum:
		print(get_fizzbuzz(n))
		n += 1

def fizz_buzz(minumum, maximum):
#	fizz_numb = 3
#	buzz_numb = 5
	n = minumum

	while n <= maximum:
		if fizzish(n, fizz_numb) and fizzish(n, buzz_numb):
			print("fizzbuzz")
		elif fizzish(n, fizz_numb):
			print("fizz")
		elif fizzish(n, buzz_numb):
			print("buzz")
		else:
			print(n)
		n += 1

fizz_buzz(minimum, maximum)
