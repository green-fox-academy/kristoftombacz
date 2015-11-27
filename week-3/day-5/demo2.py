def user_input():
	user_input = input("Please enter a string! ")
	return user_input

def reverse(string_input):
	reverse = ''
	for n in string_input:
		reverse = n + reverse
	return reverse
	
def search_palindromes(string_input):
	words = string_input.split(' ')
	palindromes = []

	for n in words:		
		i2 = 3
		while i2 <= len(n):
			i = 0
			while i <= len(n):
				if n[i:i2] == reverse(n[i:i2]) and len(n[i:i2]) >= 3:
					palindromes.append(n[i:i2])
				i += 1
			i2 += 1
	return palindromes

output = search_palindromes(user_input())
print(output)
