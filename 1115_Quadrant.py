for i in range(1000):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X == 0 or Y == 0:
        break
    elif X > 0 and Y > 0:
        print("primeiro")
    elif X > 0 and Y < 0:
        print("quarto")
    elif X < 0 and Y < 0:
        print("terceiro")
    else:
        print("segundo")