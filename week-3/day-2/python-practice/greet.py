def greet(greets, name):
	if greets == "":
		greets = "Hello"
		print(greets, name)
	else:
		print(greets, name)

greets = input("add meg a koszonest: ")
name = input("add meg a nevet: ")

greet(greets, name)
