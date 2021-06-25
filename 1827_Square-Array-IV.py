while True:
    try:
        N = int(input())
        if N >= 5 and N <= 101 and N%2!=0:
            arr = []
            b=N-1
            for i in range(N):
                new_arr = []
                for j in range(N):
                    if i==j:
                        new_arr.append(2)
                    elif j==b and b>=0:
                        new_arr.append(3)
                    else:
                        new_arr.append(0)
                arr.append(new_arr)
                b -= 1
            for_one = int(N/3)
            for i in range(for_one,N-for_one):
                for j in range(for_one,N-for_one):
                    arr[i][j] = 1
            middle = int((N + 1) / 2)
            arr[middle-1][middle-1] = 4
            for i in range(N):
                for j in range(N):
                    print(arr[i][j], end="")
                print("")
            print("")

    except EOFError:
        break