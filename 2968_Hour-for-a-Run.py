import math
v, n = map(int, input().split())
ans = []
x = 10
for i in range(9):
    ans.append(math.ceil((v*n)*(x/100)))
    x += 10
for i in range(len(ans)-1):
    print(int(ans[i]), end=" ")
print(int(ans[len(ans)-1]))

# 10% wrong answer