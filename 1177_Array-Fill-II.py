T = int(input())
if T>=2 and T<=50:
    list_num = []
    x = 0
    for i in range(1000):
        list_num.append(x)
        x += 1
        if x == T:
            x = 0
    for i in  range(len(list_num)):
        print("N[{}] = {}".format(i,list_num[i]))