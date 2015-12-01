students = [
	{'name': 'tibi', 'age': 8},
	{'name': 'adorjan', 'age': 9},
	{'name': 'agoston', 'age': 6},
	{'name': 'aurel', 'age': 7},
	{'name': 'dezso', 'age': 12}
]

students_atleast_8 = []
student_ages_starting_with_a = []

def add(student_list):
	for n in student_list:
		if n['age'] >= 8:
			students_atleast_8.append(n['name'])
	return students_atleast_8

def add2(student_list):
	for n in student_list:
		if n['name'][0] == 'a':
			student_ages_starting_with_a.append(n['age'])
	return student_ages_starting_with_a

print(add(students))
print(add2(students))
