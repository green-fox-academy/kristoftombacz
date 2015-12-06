def is_complete(numbers):
	a = sum(range(len(numbers)))

	if len(numbers) != 9:
		return False
	if a != 45:
		return False
