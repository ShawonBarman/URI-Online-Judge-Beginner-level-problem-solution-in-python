n = int(input())
votes = []
while n != 0:
    n -= 1
    v = int(input())
    votes.append(v)

x = votes[0]
votes.sort(reverse=True)

if x == votes[0]:
    print("S")
else:
    print("N")