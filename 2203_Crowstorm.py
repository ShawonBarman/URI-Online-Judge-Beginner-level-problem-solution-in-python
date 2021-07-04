#(Xf, Yf) -> coordinates of Fiddlesticks
# (4, 6)
#(Xi, Yi) -> initial coordinates of invader
# (22, 6)
#Vi -> the speed of the invader
# 0
# 1
#R1 -> the ultimate of casting radius of crows
# 16
#R2 -> the ultimate of flight radius of crows
# 2
import math
while True:
    try:
        numbers = list(map(int, input().split()))[:7]
        xf = numbers[0]
        yf = numbers[1]
        xi = numbers[2]
        yi = numbers[3]
        vi = numbers[4]
        r1 = numbers[5]
        r2 = numbers[6]
        distance = math.sqrt(math.pow((xi-xf),2) + math.pow((yi-yf),2))
        ans = distance + (vi * 1.5)
        r = r1 + r2
        if ans < r:
            print("Y")
        else:
            print("N")
    except EOFError:
        break