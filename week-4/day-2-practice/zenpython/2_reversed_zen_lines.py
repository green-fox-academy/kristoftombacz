first = open('reversed_zen_lines.txt')
first_write = open('2_reversed_zen_lines_result.txt', 'w')

first_read = first.readlines()

def reversed_zen_lines(text):
	valami = ''
	for n in text:
		 valami += n[::-1]
	return valami

reversed_zen_lines(first_read)
first_write.write(reversed_zen_lines(first_read))

first.close()
first_write.close()
