while True:
    n = int(input())
    if n == 0:
        break
    xi = list(map(int, input().split()))[:n*2]
    xi.sort(reverse=True)
    p = []
    for i in range(n):
        p.append(xi[i] + xi[len(xi) - 1 - i])

    print(max(p),min(p))