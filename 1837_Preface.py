a, b = input().split()
a = int(a)
b = int(b)
global q
global r
for r in range(abs(b)):
    if ((a - r) % b) == 0:
        q = int((a - r)/b)
        break
print("{} {}".format(q,r))