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
    if num>1:
        half_num = 0
        if num% 2 != 0:
            half_num = int((num+1)/2)
        else:
            half_num = int(num/2)
        a = 0
        b = num
        for k in range(1,half_num+1):
            for i in range(a,b):
                for j in range(a,b):
                    arr[i][j] = k
            a += 1
            b -= 1
    for i in range(num):
        tx = ''
        for j in range(num):
            tx += " %3d" % arr[i][j]
        print(tx[1:])
    print("")