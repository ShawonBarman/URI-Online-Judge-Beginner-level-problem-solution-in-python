N = int(input())
if N>1 and N<1000:
    for i in range(1,11):
        print("{} x {} = {}".format(i,N,i*N))