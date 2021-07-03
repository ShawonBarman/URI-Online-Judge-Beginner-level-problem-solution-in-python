N = int(input())
R = list(map(int, input().split()))[:N]
if N==2 and R[0] > R[1]:
    x = 2
else:
    x = 0
    for i in range(1,N):
        if R[i-1] > R[i]:
            x = i + 1
            break
print(x)