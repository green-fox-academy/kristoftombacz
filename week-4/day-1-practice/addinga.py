ag = input('Adj meg egy stringet: ')

def addinga(string):
	return string + 'a'

ag = addinga(ag)
print(ag)

ag2 = ['rep', 'macsk', 'cic', 'alm', 'Ann', 'kacs']

for i in range(len(ag2)):
	ag2[i] = addinga(ag2[i])

print(ag2)
