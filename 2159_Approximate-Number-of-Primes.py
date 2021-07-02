import math
num = int(input())
P = num / math.log(num)
M = 1.25506 * P
print("{:.1f} {:.1f}".format(P, M))