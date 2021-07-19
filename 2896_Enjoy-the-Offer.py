t = int(input())
while t != 0:
    t -= 1
    n, k = map(int, input().split())
    ans = int((n%k) + (n/k))
    print(ans)