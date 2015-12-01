temp = input('Enter a number: ')
a = int(temp)

def faktor(a):
	s = 1
	i = 0
	while i != a:
		s *= a - i 
		i += 1
	return s

print(faktor(a))



def faktorrekur(a):
	if a == 1:
		return 1
	else:
		return faktorrekur(a - 1) * a

print(faktorrekur(a))
