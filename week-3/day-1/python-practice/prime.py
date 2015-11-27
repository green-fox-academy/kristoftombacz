temp = input('adj meg egy szamot: ')
number = int(temp)
base = 2
trueorfalse = False;

for k in range(base, number):
    if number % k == 0:
    	trueorfalse = False
        break
    elif number % k != 0:
    	trueorfalse = True

if trueorfalse == True:
    print("ez egs prim")
else:
    print("ez nem egny primmm")
