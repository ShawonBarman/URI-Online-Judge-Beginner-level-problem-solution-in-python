N = int(input())
T = list(map(int,input().split()))[:N]
minimum_hit = min(T)
ans = T.index(minimum_hit) + 1
print(ans)