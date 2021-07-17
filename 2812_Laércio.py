n = int(input())
while n != 0:
    n -= 1
    m = int(input())
    numbers = list(map(int, input().split()))[:m]
    arr = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            arr.append(numbers[i])
    if len(arr) == 0:
        continue
    else:
        new_arr = []
        while len(arr) != 0:
            maxi = max(arr)
            mini = min(arr)
            if maxi in arr:
                new_arr.append(maxi)
                arr.pop(arr.index(maxi))
            if mini in arr:
                new_arr.append(mini)
                arr.pop(arr.index(mini))
        for i in range(len(new_arr)-1):
            print(new_arr[i], end=" ")
        print(new_arr[len(new_arr)-1])
    if n != 0:
        print("")

#this solution give me 5% presentation error.