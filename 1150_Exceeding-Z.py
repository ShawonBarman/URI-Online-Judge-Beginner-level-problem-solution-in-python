X = int(input())
while(True):
    Z = int(input())
    if Z > X:
        break
sum=0
count=1
for i in range(X,Z):
    sum+=i
    if sum<=Z:
        count+=1
print(count)