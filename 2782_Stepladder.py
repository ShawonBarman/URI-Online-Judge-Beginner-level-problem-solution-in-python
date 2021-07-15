n = int(input())
arr = list(map(int, input().split()))[:n]
if n == 1 or n == 2:
    print(1)
else:
    count = 1
    x = arr[0] - arr[1]
    for i in range(2, n):
        y = arr[i-1] - arr[i]
        if y != x:
            x = y
            count += 1
    print(count)