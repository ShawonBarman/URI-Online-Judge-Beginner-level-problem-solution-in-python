def fib():
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2,30):
        arr.append(arr[i-1]+arr[i-2])
    numbers = []
    for i in range(100025):
        numbers.append(i)
    new_arr = []
    for i in range(100025):
        if numbers[i] in arr:
            continue
        else:
            new_arr.append(numbers[i])
    return new_arr
new_arr = fib()
k = int(input())
print(new_arr[k-1])