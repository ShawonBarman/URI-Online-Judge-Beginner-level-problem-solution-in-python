while True:
    try:
        N, M = input().split()
        arr = []
        for i in range(int(N)):
            arr.append(list(map(int, input().split()))[:M])
    except EOFError:
        break

'''Hey, I am sorry! this solution will come in future. Please wait...'''