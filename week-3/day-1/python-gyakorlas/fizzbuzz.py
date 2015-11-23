ize = input ('adj meg egy szamot: ')
szam = int(ize)

lt = [1] * szam
su = 1
i = 0

while i < len(lt):
    lt[i] = su

    su += 1
    i += 1

i = 0
segedgeci = 0
while i < len(lt):
    if ((lt[i] % 3) == 0) and ((lt[i] % 5) == 0):
        lt[i] = "fizzbuzz"
    elif (lt[i] % 3) == 0:
        lt[i] = "fizz"
    elif (lt[i] % 5) == 0:
        lt[i] = "buzz"
    elif (lt[i] // 10) == 3:
        lt[i] = "fizz"
    elif (lt[i] // 10) == 5:
        lt[i] = "buzz"
    elif (lt[i] // 10) == 3 and (lt[i] % 5) == 0:
        lt[i] = "fizzbuzz"
    elif (lt[i] // 10) == 5 and (lt[i] % 5) == 0:
        lt[i] = "fizzbuzz"
    else:
        pass
    i += 1

for ir in lt:
    print(ir)
