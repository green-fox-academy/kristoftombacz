temp = input('adj meg egy szamot: ')
szam = int(temp)
base = 2
trueorfalse = False;

for k in range(base, szam):
    if szam % k == 0:
        trueorfalse = False
        break
    elif szam % k != 0:
          trueorfalse = True

if trueorfalse == True:
    print("ez egs prim")
else:
    print("ez nem egny primmm")
