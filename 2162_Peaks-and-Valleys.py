N = int(input())
numbers = list(map(int, input().split()))[:N]
if N == 2 and numbers[0] == numbers[1]:
    x = 0
else:
    x = 1
    for i in range(1, N-1):
        if not((numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]) or (numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1])):
            x = 0
            break
print(x)