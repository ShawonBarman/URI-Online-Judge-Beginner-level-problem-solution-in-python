N = int(input())
for i in  range(N):
    num1, num2, num3 = input().split()
    avg = ((float(num1)*2)+(float(num2)*3)+(float(num3)*5))/(2+3+5)
    print("{0:.1f}".format(avg))