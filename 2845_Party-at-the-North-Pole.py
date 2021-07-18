n = int(input())
numbers = list(map(int, input().split()))[:n]
ans = sum(numbers)/(n/2)
print(int(ans))