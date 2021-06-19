N = int(input())
if N<10000:
    for i in range(N):
        num = int(input())
        if num == 0:
            print("NULL")
        if num > 0:
            if num%2==0:
                print("EVEN POSITIVE")
            else:
                print("ODD POSITIVE")
        if num < 0:
            if num%2==0:
                print("EVEN NEGATIVE")
            else:
                print("ODD NEGATIVE")