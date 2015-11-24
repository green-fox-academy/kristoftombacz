def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)
	
temp = input("adj meg egy sazmot: ")
ize = int(temp)
res = fibonacci(ize)
print(res)
