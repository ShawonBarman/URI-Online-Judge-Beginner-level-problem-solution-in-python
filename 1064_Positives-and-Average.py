sum = 0
count = 0
for i in range(6):
    num = input()
    if float(num)>0:
        sum += float(num)
        count+=1
avg = sum/count
print("{} valores positivos".format(count))
print("{0:.1f}".format(avg))