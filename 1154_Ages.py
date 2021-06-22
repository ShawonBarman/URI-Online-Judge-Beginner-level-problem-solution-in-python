sum = 0
count = 0
while(True):
    ages = int(input())
    if ages<0:
        break
    sum += ages
    count += 1
avg = sum/count
print("{0:.2f}".format(avg))