while True:
    m = int(input())
    if m == 0:
        break
    x = 0
    while m != 0:
        m -= 1
        l, c, r = map(int, input().split())
        if l==1 and c==1:
            x += 1
        elif c==1 and r==1:
            x += 1
        elif l==1 and r==1:
            x += 1
    print(x)

# 10% wrong answer.