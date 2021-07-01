n, m = input().split()
n = int(n)
m= int(m)
for i in range(m):
    st = input()
    if st == "fechou":
        n += 1
    else:
        n -= 1
print(n)