list_num = []
for i in range(100):
    num = int(input())
    list_num.append(num)
x = -999999
for i in range(len(list_num)):
    if list_num[i] > x:
        x = list_num[i]
print(x)
print(list_num.index(x)+1)