name_list = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']
a = list(map(int, input().split()))[:9]
s = sum(a)
count = 0
while s != 1:
    s -= 1
    count += 1
    if count == 9:
        count = 0
print(name_list[count])