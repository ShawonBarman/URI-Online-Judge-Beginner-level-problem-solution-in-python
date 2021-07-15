n, c, m = map(int, input().split())
stamped = list(map(int, input().split()))[:c]
cards = list(map(int, input().split()))[:m]
count = 0
for i in range(len(stamped)):
    if stamped[i] in cards:
        count += 1
print(len(stamped) - count)