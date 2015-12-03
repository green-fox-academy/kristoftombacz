temp = open('1_reversed_zen_order.txt')
temp_write = open('1_reversed_zen_order_result.txt', 'w')
lines = temp.readlines()

def reversed_zen_order(text):
	text = text[::-1]
	sum = ''
	for i in text:
		sum = sum + i
	return sum

temp_write.write(reversed_zen_order(lines))
reversed_zen_order(lines)

temp.close()
temp_write.close()
