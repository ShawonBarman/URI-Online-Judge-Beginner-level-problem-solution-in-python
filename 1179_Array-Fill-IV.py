par = []
impar = []
for i in range(15):
    if len(par) == 5:
        for i in range(len(par)):
            print("par[{}] = {}".format(i,par[i]))
        par.clear()
    if len(impar) == 5:
        for i in range(len(impar)):
            print("impar[{}] = {}".format(i,impar[i]))
        impar.clear()
    num = int(input())
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
for i in range(len(impar)):
    print("impar[{}] = {}".format(i, impar[i]))
for i in range(len(par)):
    print("par[{}] = {}".format(i, par[i]))