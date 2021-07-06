while True:
    try:
        N, M = input().split()
        N = int(N)
        M = int(M)
        city_arr = []
        for i in range(N):
            new_arr = list(map(int, input().split()))[:M]
            city_arr.append(new_arr)
        x, y, a, b =0, 0, 0, 0
        for i in range(N):
            if 2 in city_arr[i]:
                x = i
                y = city_arr[i].index(2)
            if 1 in city_arr[i]:
                a = i
                b = city_arr[i].index(1)
        ans = abs(y-b) + abs(x-a)
        print(ans)
    except EOFError:
        break