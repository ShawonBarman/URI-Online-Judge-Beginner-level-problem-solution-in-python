n = int(input())
m = int(input())
count = 0
new_arr = []
for i in range(m):
    x = int(input())
    if x not in new_arr:
        new_arr.append(x)
print(n - len(new_arr))