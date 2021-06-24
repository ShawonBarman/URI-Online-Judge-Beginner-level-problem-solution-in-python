while(True):
    try:
        num = int(input())
        arr = []
        for i in range(num):
            new_arr = []
            for j in range(num):
                if i == j:
                    new_arr.append(1)
                else:
                    new_arr.append(3)
            arr.append(new_arr)
        x = num - 1
        for i in range(num):
            for j in range(num):
                if j == x:
                    arr[i][j] = 2
            x -= 1

        for i in range(num):
            for j in range(num):
                print(arr[i][j], end="")
            print()
    except EOFError:
        break