while True:
    T = int(input())
    if T == 0:
        break
    arr = []
    for i in range(T):
        num = int(input())
        if num%2==0:
            arr.append((num*2)-2)
        else:
            arr.append((num*2)-1)
    for i in arr:
        print(i)