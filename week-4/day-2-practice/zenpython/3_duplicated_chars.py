temp = open('duplicated_chars.txt')
temp_write = open('3_duplicated_chars_result.txt', 'w')
lines = temp.readlines()

def duplicated_chars(text):
	for n in text:
		temp_write.write(n[::2])	

temp_write.write(dublicated_chars(lines))
duplicated_chars(lines)

temp.close()
temp_write.close()
