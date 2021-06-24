while(True):
    list_num = list(map(int,input().split()))
    if len(list_num)==1 and list_num[0]==0:
        break
    A = list_num[0]
    B = list_num[1]
    C = list_num[2]
    total_meter = int(A*B*(100/C))
    ans = 0
    for i in range(total_meter):
        if i*i <= total_meter:
            ans = i
        if i*i > total_meter:
            break
    print(ans)