X, Y = input().split()
X = int(X)
Y = int(Y)
if X>1 and X<20 and X<Y and Y<100000:
    count = 0
    for i in range(1,Y+1):
        count+=1
        if count==X:
            print(i)
            count=0
        else:
            print(i, end=" ")