n, m = map(int, input().split())
dic = {}
while n != 0:
    n -= 1
    r, v = input().split()
    dic.update({r: int(v)})
x = int(input())
characters = list(map(str, input().split()))[:x]
sum = 0
for i in range(len(characters)):
    sum += dic[characters[i]]
if sum >= m:
    print(sum)
    print("You shall pass!")
else:
    print(sum)
    print("My precioooous")