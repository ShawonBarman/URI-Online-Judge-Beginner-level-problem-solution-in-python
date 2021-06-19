count = 0
for i in range(6):
    num = input()
    if num[0]!="-":
        count+=1
print("{} valores positivos".format(count))