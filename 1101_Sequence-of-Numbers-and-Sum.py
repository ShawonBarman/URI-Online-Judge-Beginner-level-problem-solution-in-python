for i in range(1000):
    M, N = input().split()
    M = int(M)
    N = int(N)
    sum = 0
    if M<=0 or N<=0:
        break
    else:
        if M>N:
            temp = M
            M = N
            N = temp
        for i in range(M,N+1):
            print(i,end=" ")
            sum+=i
        print("Sum={}".format(sum))