C = int(input())
T = input()
list_num = []
for i in range(12):
    new_list=[]
    for j in range(12):
        num = float(input())
        new_list.append(num)
    list_num.append(new_list)
sum = 0
for i in range(12):
    sum += list_num[i][C]
if T == "S":
    print("{:.1f}".format(sum))
if T == "M":
    print("{:.1f}".format(sum/12))