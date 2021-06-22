n = int(input())
for i in range(n):
    x = int(input())
    count=0
    for i in range(2,x):
        if x%i==0:
            count+=1
            break
    if count==0:
        print("{} eh primo".format(x))
    else:
        print("{} nao eh primo".format(x))