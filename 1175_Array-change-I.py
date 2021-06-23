N = []
for i in range(20):
    num = int(input())
    N.append(num)
x = len(N)-1
for i in  range(20):
    if i == 10:
        break
    temp = N[i]
    N[i] = N[x]
    N[x] = temp
    x = x-1
for i in range(len((N))):
    print("N[{}] = {}".format(i,N[i]))
