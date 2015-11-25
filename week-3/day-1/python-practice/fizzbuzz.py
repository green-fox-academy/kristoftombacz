temp = input ('adj meg egy szamot: ')
number = int(temp)

lt = [1] * number
su = 1
i = 0

while i < len(lt):
    lt[i] = su

    su += 1
    i += 1

i = 0
base1 = 3
base2 = 5

while i < len(lt):
    if (((lt[i] % base1) == 0) or str(lt[i]) in str(base1)) and (((lt[i] % base2) == 0) or str(lt[i]) in str(base2)):
        lt[i] = "fizzbuzz"
    elif (lt[i] % base1) == 0:
        lt[i] = "fizz"
    elif (lt[i] % base1) == 0:
        lt[i] = "buzz"
      
    else:
        pass
    i += 1

for ir in lt:
    print(ir)
