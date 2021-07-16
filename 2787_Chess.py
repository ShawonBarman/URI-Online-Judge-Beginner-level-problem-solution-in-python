l = int(input())
c = int(input())
arr = []
for i in range(l):
    new_arr = []
    for j in range(c):
        new_arr.append('w')
    arr.append(new_arr)

for i in range(l):
    for j in range(c):
        if i % 2 == 0:
            if j % 2 == 1:
                arr[i][j] = 'b'
        else:
            if j % 2 == 0:
                arr[i][j] = 'b'
if arr[l-1][c-1] == 'w':
    print(1)
elif arr[l-1][c-1] == 'b':
    print(0)