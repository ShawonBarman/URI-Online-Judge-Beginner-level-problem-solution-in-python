import math

while True:
    try:
        m = int(input())
        arr = []
        for i in range(m):
            num = int(input())
            arr.append(num)
        n = int(input())
        sum = int()
        a = 0
        ind = m
        while True:
            if n * a >= m:
                break
            ind = m-(n*a)
            if ind <= 0:
                break
            sum += arr[ind-1]
            a += 1
        flag = True
        x = int(math.sqrt(sum))
        if sum != 2 and sum % 2 == 0 or sum == 1:
            flag = False
        else:
            for i in range(3, x+1):
                if sum % i == 0:
                    flag = False
        if flag == True:
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
    except EOFError:
        break