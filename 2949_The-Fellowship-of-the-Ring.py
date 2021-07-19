a, e, h, m, x = 0, 0, 0, 0, 0
n = int(input())
while n != 0:
    n -= 1
    name, char = input().split()
    if char == "A":
        a += 1
    elif char == "E":
        e += 1
    elif char == "H":
        h += 1
    elif char == "M":
        m += 1
    elif char == "X":
        x += 1
print(x,"Hobbit(s)")
print(h,"Humano(s)")
print(e,"Elfo(s)")
print(a,"Anao(s)")
print(m,"Mago(s)")