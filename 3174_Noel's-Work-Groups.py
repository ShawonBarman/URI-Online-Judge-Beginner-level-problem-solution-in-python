n = int(input())
sum = 0
while n != 0:
    n -= 1
    e, g, h = input().split()
    h = int(h)
    if g == "bonecos":
        sum += (h / 8)
    elif g == "arquitetos":
        sum += (h / 4)
    elif g == "musicos":
        sum += (h / 6)
    elif g == "desenhistas":
        sum += (h / 12)
print(int(sum))