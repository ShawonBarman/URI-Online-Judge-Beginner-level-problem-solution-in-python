X = int(input())
Y = int(input())
if X>Y:
    temp = X
    X = Y
    Y = temp
for i in range(X+1,Y):
    if i%5==2 or i%5==3:
        print(i)