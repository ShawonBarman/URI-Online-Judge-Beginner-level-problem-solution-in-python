X = int(input())
Y = int(input())
sum = 0
if X>Y:
    temp = X
    X = Y
    Y = temp
for i in range(X,Y+1):
    if i%13!=0:
        sum+=i
print(sum)