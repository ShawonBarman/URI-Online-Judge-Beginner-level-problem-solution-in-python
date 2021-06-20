count = 0
sum = 0
global x
while(True):
    while(True):
        num = float(input())
        if num >= 0 and num <= 10:
            count+=1
            sum+=num
        else:
            print("nota invalida")
        if count == 2:
            break
    print("media = {0:.2f}".format(sum/count))
    count = 0
    sum = 0
    while(True):
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        if x == 1 or x == 2:
            break
    if x == 1:
        continue
    if x ==2:
        break


