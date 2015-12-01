lada = {
	'color': 'red',
	'type': 'Lada 1200',
	'km': 40000,
}

tesla = {
	'color': 'pink',
	'type': 'Tesla S',
	'km': 1200,
}

def initCar(color, type, km):
	car = {'color': '', 'type': '', 'km': ''}
	car['color'] = color
	car['type'] = type
	car['km'] = km

	return car
	

def ride(car, km):
	car['km'] += km

lada = initCar('red', 'Lada 1200', 40000)
tesla = initCar('pink', 'Tesla S', 1200)
ifa = initCar('barna', 'Ifa', 30000000)

ride(ifa, 220)

print(ifa)
print(lada)
