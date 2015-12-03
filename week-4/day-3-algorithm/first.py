students = [    
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
	{'name': 'Gerzson', 'age': 10, 'candies': 1}, 
	{'name': 'Aurel', 'age': 7, 'candies': 3},
	{'name': 'Zsombor', 'age': 12, 'candies': 5},
	{'name': 'Olaf', 'age': 12, 'candies': 7},  
        {'name': 'Teodor', 'age': 3, 'candies': 2}  
]



def student_list(list):
	sum = 0
	for n in list:
		if n['candies'] > 4:
			sum += 1
	return sum

print(student_list(students))
