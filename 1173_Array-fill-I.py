list_num = []
V = int(input())
if V < 50:
    list_num.append(V)
    print("N[{}] = {}".format(0, list_num[0]))
    for i in range(1, 10):
        V = V * 2
        list_num.append(V)
        print("N[{}] = {}".format(i, list_num[i]))