N = int(input())
for i in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    sum = 0
    count = 0
    while(True):
        if X%2 != 0:
            sum += X
            count += 1
        if count == Y:
            break
        X += 1
    print(sum)