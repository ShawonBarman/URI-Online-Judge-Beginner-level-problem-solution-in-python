n = int(input())
v = 0
g = 0
while n != 0:
    n -= 1
    t, c = input().split()
    if t == "V":
        v += int(c)
    if t == "G":
        g += int(c)
if g > v:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")