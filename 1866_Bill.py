C = int(input())
for i in range(C):
    num = int(input())
    sum = 0
    for j in range(1,num+1):
        if j%2 != 0:
            sum += 1
        else:
            sum -= 1
    print(sum)