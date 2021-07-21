n = int(input())
while n != 0:
    n -= 1
    john_total = 0
    mary_total = 0
    for i in range(6):
        x, d = map(int, input().split())
        if i <= 2:
            john_total += (x * d)
        else:
            mary_total += (x * d)
    if john_total > mary_total:
        print("JOAO")
    else:
        print("MARIA")