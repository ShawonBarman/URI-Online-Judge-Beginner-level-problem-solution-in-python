n = int(input())
sum = 0
while n != 0:
    n -= 1
    c, p = map(int, input().split())
    sum += (c/p)
if sum <= 1:
    print("OK")
else:
    print("FAIL")