while(True):
    num = int(input())
    if num == 0:
        break
    arr = []
    for i in range(num):
        new_arr = []
        for j in range(num):
            new_arr.append(1)
        arr.append(new_arr)
    a=0
    x=1
    for i in range(num):
        for j in range(a,num):
            arr[a][j] = x
            x += 1
        x=1
        a+=1
    y=1
    a=0
    for i in range(num):
        for k in range(a,num):
            arr[k][a] = y
            y += 1
        y=1
        a += 1

    for i in range(num):
        tx = ''
        for j in range(num):
            tx += " %3d" % arr[i][j]
        print(tx[1:])
    print("")