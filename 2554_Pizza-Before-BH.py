while True:
    try:
        n, d = map(int, input().split())
        x = False
        date = ''
        for i in range(d):
            arr = list(map(str,input().split()))
            s = arr[1:]
            flag = 0
            for e in s:
                if e == '1':
                    flag += 1
            if flag == n and not x:
                date = arr[0]
                x = True

        if x:
            print(date)
        else:
            print('Pizza antes de FdI')

    except EOFError:
        break