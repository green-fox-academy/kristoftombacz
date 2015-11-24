temp = input('adj meg egy szamot, addig mutatom a primeket: ')
szam = int(temp)
lst = range(2, szam)

for n in lst:
    for secondfor in range(2, n):
        if n % secondfor == 0:
            break
    else:
        if n != 2:
            print (n)
