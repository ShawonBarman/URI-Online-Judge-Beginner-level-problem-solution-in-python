N = int(input())
for i in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if Y == 0:
        print("divisao impossivel")
    else:
        print("{0:.1f}".format(X/Y))