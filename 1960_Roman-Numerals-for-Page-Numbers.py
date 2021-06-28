#I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
def oneDigit(N):
    if N == 1:
        print("I",end="")
    elif N == 2:
        print("II",end="")
    elif N == 3:
        print("III",end="")
    elif N == 4:
        print("IV",end="")
    elif N == 5:
        print("V",end="")
    elif N == 6:
        print("VI",end="")
    elif N == 7:
        print("VII",end="")
    elif N == 8:
        print("VIII",end="")
    elif N == 9:
        print("IX",end="")
def twoDigit(N):
    d = int(N/10)
    N -= (d*10)
    if d == 1:
        print("X",end="")
    elif d == 2:
        print("XX",end="")
    elif d == 3:
        print("XXX",end="")
    elif d == 4:
        print("XL",end="")
    elif d == 5:
        print("L",end="")
    elif d == 6:
        print("LX",end="")
    elif d == 7:
        print("LXX",end="")
    elif d == 8:
        print("LXXX",end="")
    elif d == 9:
        print("XC",end="")
    oneDigit(N)
def threeDigit(N):
    e = int(N/100)
    N -= (e*100)
    if e == 1:
        print("C",end="")
    elif e == 2:
        print("CC",end="")
    elif e == 3:
        print("CCC",end="")
    elif e == 4:
        print("CD",end="")
    elif e == 5:
        print("D",end="")
    elif e == 6:
        print("DC",end="")
    elif e == 7:
        print("DCC",end="")
    elif e == 8:
        print("DCCC",end="")
    elif e == 9:
        print("CM",end="")
    twoDigit(N)

N = int(input())
if N < 10:
    oneDigit(N)
elif N < 100:
    twoDigit(N)
elif N < 1000:
    threeDigit(N)
print()