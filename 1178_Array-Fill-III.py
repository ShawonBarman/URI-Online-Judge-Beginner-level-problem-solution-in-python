x = float(input())
list_num = []
list_num.append(x)
for i in range(1,100):
    x = x/2
    list_num.append(x)
for i in range(len(list_num)):
    print("N[{}] = {:.4f}".format(i,list_num[i]))