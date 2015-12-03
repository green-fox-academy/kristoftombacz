 
x = [1,2,3,4,5,6,7,8,9,10]
y = 7
k = x[0]
v = len(x)
while ((v+k)/2) != v:
	if x[int((k+v)/2)] < y:
		k = (k+v)/2
	else:
		v = (k+v)/2
print(k)
