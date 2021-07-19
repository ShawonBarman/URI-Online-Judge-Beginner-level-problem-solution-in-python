n = int(input())
count = 0
for i in range(n):
    num = int(input())
    if num == 1:
        continue
    elif num == 2:
        count += 1
    elif num == 3:
        count += 1
print(count)