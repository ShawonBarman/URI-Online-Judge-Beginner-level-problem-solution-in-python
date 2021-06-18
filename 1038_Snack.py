X, Y = input().split()
X = int(X)
Y = int(Y)
if X == 1:
    print("Total: R$ {0:.2f}".format(Y * 4.00))
if X == 2:
    print("Total: R$ {0:.2f}".format(Y * 4.50))
if X == 3:
    print("Total: R$ {0:.2f}".format(Y * 5.00))
if X == 4:
    print("Total: R$ {0:.2f}".format(Y * 2.00))
if X == 5:
    print("Total: R$ {0:.2f}".format(Y * 1.50))