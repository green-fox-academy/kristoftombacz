tmp = input ('irj be egy szamot tojas! ')
ins=int(tmp)
ize = ""
if (ins > 3999):
    print("tul nagy a szam, max 3999")
if (ins // 1000) == 3:
    ize = ize + "MMM"
    ins = ins - 3000
elif (ins // 1000) == 2:
    ize = ize + "MM"
    ins = ins - 2000
elif (ins // 1000) == 1:
    ize = ize + "M"
    ins = ins - 1000
if (ins // 100) == 9:
    ize = ize + "CM"
    ins = ins - 900
elif (ins // 100) == 8:
    ize = ize + "DCCC"
    ins = ins - 800
elif (ins // 100) == 7:
    ize = ize + "DCC"
    ins = ins - 700
elif (ins // 100) == 6:
    ize = ize + "DC"
    ins = ins - 600
elif (ins // 100) == 5:
    ize = ize + "D"
    ins = ins - 500
elif (ins // 100) == 4:
    ize = ize + "CD"
    ins = ins - 400
elif (ins // 100) == 3:
    ize = ize + "CCC"
    ins = ins - 300
elif (ins // 100) == 2:
    ize = ize + "CC"
    ins = ins - 200
elif (ins // 100) == 1:
    ize = ize + "C"
    ins = ins - 100
if (ins // 10) == 9:
    ize = ize + "XC"
    ins = ins - 90
elif (ins // 10) == 8:
    ize = ize + "LXXX"
    ins = ins - 80
elif (ins // 10) == 7:
    ize = ize + "LXX"
    ins = ins - 70
elif (ins // 10) == 6:
    ize = ize + "LX"
    ins = ins - 60
elif (ins // 10) == 5:
    ize = ize + "L"
    ins = ins - 50
elif (ins // 10) == 4:
    ize = ize + "XL"
    ins = ins - 40
elif (ins // 10) == 3:
    ize = ize + "XXX"
    ins = ins - 30
elif (ins // 10) == 2:
    ize = ize + "XX"
    ins = ins - 20
elif (ins // 10) == 1:
    ize = ize + "X"
    ins = ins - 10
if (ins // 1) == 9:
    ize = ize + "IX"
    ins = ins - 9
elif (ins // 1) == 8:
    ize = ize + "IIX"
    ins = ins - 8
elif (ins // 1) == 7:
    ize = ize + "VII"
    ins = ins - 7
elif (ins // 1) == 6:
    ize = ize + "VI"
    ins = ins - 6
elif (ins // 1) == 5:
    ize = ize + "V"
    ins = ins - 5
elif (ins // 1) == 4:
    ize = ize + "IV"
    ins = ins - 4
elif (ins // 1) == 3:
    ize = ize + "III"
    ins = ins - 3
elif (ins // 1) == 2:
    ize = ize + "II"
    ins = ins - 2
elif (ins // 10) == 1:
    ize = ize + "I"
    ins = ins - 1
print(ize)
