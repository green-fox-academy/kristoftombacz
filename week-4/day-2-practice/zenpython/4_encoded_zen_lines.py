temp = open('encoded_zen_lines.txt')
temp_write = open('4_encoded_zen_lines_result.txt', 'w')
lines = temp.read()

def encoded_zen_lines(text):
	sum = ''
	for n in text:
		if n == ' ':
			sum += ' '
		elif n == '\n':
			sum += '\n'
		elif n != ' ':
			sum += chr((ord(n)-1))
	return sum

encoded_zen_lines(lines)
temp_write.write(encoded_zen_lines(lines))

temp.close()
temp_write.close()
