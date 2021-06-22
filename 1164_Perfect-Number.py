N = int(input())
for i in range(N):
    x = int(input())
    sum=0
    for i in range(1,x):
        sum += i
        if sum == x or sum > x:
            break
    if sum == x:
        print("{} eh perfeito".format(x))
    else:
        print("{} nao eh perfeito".format(x))