X = int(input())
Y = int(input())
sum = 0
if X<Y:
    for i in range(X,Y+1):
        if i%2!=0:
            sum+=i
else:
    for i in range(Y+1,X):
        if i % 2 != 0:
            sum += i
print(sum)