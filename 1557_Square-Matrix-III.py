while(True):
    num = int(input())
    if num==0:
        break
    arr = []
    y = 1
    for i in range(num):
        new_arr = []
        x = y
        for j in range(num):
            new_arr.append(x)
            x = x*2
        arr.append(new_arr)
        y = y*2

    T = len(str(arr[num-1][num-1]))
    for i in range(num):
        for j in range(num):
            arr[i][j] = str(arr[i][j])
            while len(arr[i][j]) < T:
                arr[i][j] = ' ' + arr[i][j]
        M = ' '.join(arr[i])
        print(M)
    print()