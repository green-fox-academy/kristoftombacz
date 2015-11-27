def reverse(in_list):
	out_list = []

	i = len(in_list)-1
	
	while i >= 0:
		out_list.append(in_list[i])
		i -= 1

	return out_list

output = reverse([1,2,3,4])
print(output)
