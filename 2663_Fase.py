n = int(input())
k = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
arr.sort(reverse=True)
x = 0
for i in range(n):
    x += 1
    if x == k:
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                break
            x += 1
        break
print(x)