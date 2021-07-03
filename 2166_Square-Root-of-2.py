def sqr(n):
    if n == 0:
        return 2
    x = 2+1/sqr(n-1)
    return x

N = int(input())
ans = sqr(N) - 1
print("{:.10f}".format(ans))