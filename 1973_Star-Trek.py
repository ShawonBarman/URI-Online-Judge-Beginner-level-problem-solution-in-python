N = int(input())
numbers = list(map(int, input().split()))[:N]
sum = sum(numbers)
x = [0] * N
i = 0
while i >= 0 and i < N:
    result = numbers[i]%2
    if numbers[i] > 0:
        numbers[i] -= 1
        x[i] = 1
        sum -= 1
    if result:
        i += 1
    else:
        i -= 1

print(x.count(1), sum)