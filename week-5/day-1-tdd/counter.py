def count_letters(text):
	dic = {}
	for n in text:
		if n in dic:
			dic[n] += 1 
		else:
			dic[n] = 1
	return dic
