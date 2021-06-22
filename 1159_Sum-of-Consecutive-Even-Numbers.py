while (True):
    X = int(input())
    if X==0:
        break
    else:
        sum = 0
        count = 0
        while(True):
            if X%2==0:
                sum += X
                count += 1
            if count == 5:
                break
            X += 1
        print(sum)