temp = input('meddig menjen a fibonacci? ')
szam = int(temp)

var1 = 0
var2 = 1
swap = 0
print(swap)

while szam > var2:
    print(var2)
    swap = var1
    var1 = var2
    var2 = swap + var2
