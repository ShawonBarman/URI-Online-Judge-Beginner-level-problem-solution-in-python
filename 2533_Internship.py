while True:
    try:
        M = int(input())
        sum1 = 0
        sum2 = 0
        for i in range(M):
            N, C = input().split()
            sum1 += (int(N) * int(C))
            sum2 += int(C)
        ans = sum1 / (sum2*100)
        print("{:.4f}".format(ans))
    except EOFError:
        break