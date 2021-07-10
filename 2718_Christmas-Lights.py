n = int(input())
for i in range(n):
    num = int(input())
    binary = bin(num)
    ans = binary[2:]
    count = 0
    arr = []
    for i in range(len(ans)):
        if ans[i] == '0':
            arr.append(count)
            count = 0
        elif ans[i] == '1':
            count += 1
    arr.append(count)
    print(max(arr))