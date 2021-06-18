a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a+b>c and a+c>b and b+c>a:
    print("Perimetro = {0:.1f}".format(a+b+c))
else:
    print("Area = {0:.1f}".format((1/2)*(a+b)*c))