while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))[:n]
        time = list(map(int, input().split()))[:n]
        count = 0
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        ans = sum(time)+count
        print(ans)
    except EOFError:
        break

#Time limit exceeded