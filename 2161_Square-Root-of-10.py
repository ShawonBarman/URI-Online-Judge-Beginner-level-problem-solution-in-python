def sqr(n):
    if n == 0:
        return 6
    x = 6+1/sqr(n-1)
    return x

N = int(input())
ans = sqr(N) - 3
print("{:.10f}".format(ans))