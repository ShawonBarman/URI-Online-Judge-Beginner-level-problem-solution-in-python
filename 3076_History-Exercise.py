import math
while True:
    try:
        n = int(input())
        if n >= 1 and n <= 100:
            print(1)
        else:
            ans = n / 100
            print(math.ceil(ans))
    except EOFError:
        break