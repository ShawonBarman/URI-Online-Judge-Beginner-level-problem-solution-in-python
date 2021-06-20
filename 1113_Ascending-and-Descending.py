for i in range(1000):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X==Y:
        break
    elif X>Y:
        print("Decrescente")
    else:
        print("Crescente")