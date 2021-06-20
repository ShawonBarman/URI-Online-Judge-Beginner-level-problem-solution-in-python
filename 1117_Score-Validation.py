count = 0
sum = 0
for i in range(1000):
    num = float(input())
    if num >= 0 and num <= 10:
        count+=1
        sum+=num
    else:
        print("nota invalida")
    if count == 2:
        break
print("media = {0:.2f}".format(sum/count))