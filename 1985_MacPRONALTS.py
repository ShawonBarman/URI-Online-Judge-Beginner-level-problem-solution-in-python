p = int(input())
if p>=1 and p<=5:
    sum = 0
    for i in range(p):
        q, r = input().split()
        q = int(q)
        r = float(r)
        if q == 1001:
            sum += (r*1.50)
        elif q == 1002:
            sum += (r*2.50)
        elif q == 1003:
            sum += (r*3.50)
        elif q == 1004:
            sum += (r*4.50)
        elif q == 1005:
            sum += (r*5.50)
    print("{:.2f}".format(sum))