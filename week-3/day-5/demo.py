def user_input():
	user_input = input("Please enter a string! ")
	return user_input

def create_palindrome(string_input):
	reverse = ''	
	for n in string_input:
		reverse = n + reverse

	return string_input + reverse

output = create_palindrome(user_input())
print(output)
