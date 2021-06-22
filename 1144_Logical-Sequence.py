N = int(input())
a = 0
for i in range(N):
    a+=1
    for j in range(1):
        b=a*a
        c=a*a*a
        print(a,b,c)
    for k in range(1):
        b = (a*a)+1
        c = (a*a*a)+1
        print(a, b, c)

