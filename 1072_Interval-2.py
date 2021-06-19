X = int(input())
count_in = 0
count_out = 0
if X<10000:
    for i in range(X):
        num = int(input())
        if num>=10 and num<=20:
            count_in+=1
        else:
            count_out+=1
print("{} in".format(count_in))
print("{} out".format(count_out))