import math
while True:
    try:
        h, m = map(int, input().split())
        x = list(map(float, input().split()))
        t = (h * 60) // m
        media = sum(x) / t
        s = 0
        for i in range(t):
            s += (x[i] - media) ** 2
        print("{:.5f}".format(math.sqrt((s) / (t - 1))))
    except EOFError:
        break