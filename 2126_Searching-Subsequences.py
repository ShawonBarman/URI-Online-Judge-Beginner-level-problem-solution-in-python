a = 0
while True:
    try:
        N1 = input()
        N2 = input()
        a += 1
        count = N2.count(N1)
        if count > 0:
            pos = N2.rfind(N1)
            print("Caso #{}:".format(a))
            print("Qtd.Subsequencias: {}".format(count))
            print("Pos: {}".format(pos+1))
        else:
            print("Caso #{}:".format(a))
            print("Nao existe subsequencia")
        print()
    except EOFError:
        break