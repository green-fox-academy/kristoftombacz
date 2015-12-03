temp = open('reversed_zen_lines.txt')
temp_write = open('2_reversed_zen_lines_result.txt', 'w')
lines = temp.readlines()

def reversed_zen_lines(text):
	sum = ''
	for n in text:
		 sum += n[::-1]
	return sum

reversed_zen_lines(lines)
temp_write.write(reversed_zen_lines(lines))

temp.close()
temp_write.close()
