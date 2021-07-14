n = int(input())
e = list(map(int,input().split()))[:2]
a = []
a.append(list(map(int, input().split()))[:n])
a.append(list(map(int, input().split()))[:n])
t = []
t.append(list(map(int, input().split()))[:n-1])
t.append(list(map(int, input().split()))[:n-1])
x = list(map(int,input().split()))[:2]
sum = 0
temp = 9999999
for i in range(2):
    for j in range(n):
            sum += a[i][j]
    sum += e[i] + x[i]
    if sum < temp:
        temp = sum
    sum = 0
print(temp)

#solution coming in future
