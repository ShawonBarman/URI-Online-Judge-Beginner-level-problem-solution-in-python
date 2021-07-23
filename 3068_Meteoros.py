import math
a = 1
while True:
    x1, y1, x2, y2 =map(int, input().split())
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    n = int(input())
    m = n
    total = 0
    if n > 0:
        while n != 0:
            n -= 1
            x, y = map(int, input().split())
            new_x = (x1-x)*(x1-x)
            new_y = (y1-y)*(y1-y)
            ans = math.sqrt(new_x+new_y)
            total += int(ans)

        print("Teste {}\n{}".format(a, int(total/m)))
        a += 1

#error this code. solution will come in future