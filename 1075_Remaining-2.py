N = int(input())
if N<10000:
    for i in range(1,10001):
        if i%N == 2:
            print(i)