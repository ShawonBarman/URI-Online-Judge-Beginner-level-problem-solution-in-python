list_num = list(map(int, input().split(" ")))
A = list_num[0]
for i in range(1,len(list_num)+1):
    k = list_num[i]
    if k>0:
        N = k
        break
sum=0
for i in range(N):
    sum = sum + A + i
print(sum)