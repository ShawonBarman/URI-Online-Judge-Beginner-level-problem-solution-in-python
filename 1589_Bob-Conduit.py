T = int(input())
if T<=10000:
    for i in range(T):
        R1, R2 = input().split()
        R1 = int(R1)
        R2 = int(R2)
        print(R1+R2)