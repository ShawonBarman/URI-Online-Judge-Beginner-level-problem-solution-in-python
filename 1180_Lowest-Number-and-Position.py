N = int(input())
if N>1 and N<1000:
    X = list(map(int, input().split()))[:N]
    smallest = 999999
    for i in range(len(X)):
        if X[i] < smallest:
            smallest = X[i]
    print("Menor valor: {}".format(smallest))
    print("Posicao: {}".format(X.index(smallest)))