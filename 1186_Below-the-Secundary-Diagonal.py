T = input()
list_num = []
for i in range(12):
    new_list=[]
    for j in range(12):
        num = float(input())
        new_list.append(num)
    list_num.append(new_list)
sum = 0
a = 12
for i in range(1,12):
    a -= 1
    for j in range(a,12):
        sum += list_num[i][j]
if T == "S":
    print("{:.1f}".format(sum))
if T == "M":
    print("{:.1f}".format(sum/66))