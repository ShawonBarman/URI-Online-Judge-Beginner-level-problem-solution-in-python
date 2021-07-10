while True:
    try:
        n = int(input())
        x = list(map(int, input().split()))[:n]
        sum1 = x[0] + x[1]
        sum2 = sum(x[2:])
        dif = sum2 - sum1
        for i in range(3,len(x)):
            new_dif = sum(x[i:]) - sum(x[:i])
            if new_dif < 0:
                break
            dif = new_dif
        print(dif)
    except EOFError:
        break