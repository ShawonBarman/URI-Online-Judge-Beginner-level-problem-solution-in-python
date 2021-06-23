list_num = []
for i in range(10):
    num = int(input())
    list_num.append(num)
for i in  range(len(list_num)):
    if list_num[i] <= 0:
        list_num[i] = 1
    print("X[{}] = {}".format(i,list_num[i]))