import math
c = int(input())
while c != 0:
    c -= 1
    n, m = map(int, input().split())
    ans = int(math.pow(n, m))
    if ans > 0:
        digits = int(math.log10(ans)) + 1
    elif ans == 0:
        digits = 1
    else:
        digits = int(math.log10(-ans)) + 2
    print(digits)