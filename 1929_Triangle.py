lengths = list(map(int, input().split()))[:4]
a = lengths[0]
b = lengths[1]
c = lengths[2]
d = lengths[3]
if a + b > c and b + c > a and a + c > b:
    print('S')
elif b + c > d and c + d > b and b + d > c:
    print('S')
elif a + c > d and c + d > a and a + d > c:
    print('S')
elif a + b > d and b + d > a and a + d > b:
    print('S')
else:
    print('N')