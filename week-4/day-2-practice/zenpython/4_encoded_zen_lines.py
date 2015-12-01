temp = open('encoded_zen_lines.txt')
temp_write = open('4_encoded_zen_lines_result.txt', 'w')

lines = temp.read()

def encoded_zen_lines(text):
	var2 = ''
	for n in text:
		if n == ' ':
			var2 += ' '
		
		elif n == '\n':
			var2 += '\n'

		elif n != ' ':
			var2 += chr((ord(n)-1))
			
	return var2


encoded_zen_lines(lines)
temp_write.write(encoded_zen_lines(lines))

temp.close()
temp_write.close()
				
