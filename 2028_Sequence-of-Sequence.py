X = 0
while True:
    try:
        series = [0]
        N = int(input())
        X += 1
        for i in range(N + 1):
            for j in range(i):
                series.append(i)
        if N == 0:
            print("Caso {}: {} numero".format(X, len(series)))
        else:
            print("Caso {}: {} numeros".format(X, len(series)))
        print(series[0],end="")
        for i in range(1, len(series)):
            print(" {}".format(series[i]),end="")
        print("\n")
    except EOFError:
        break