while True:
    try:
        T = int(input())
        sign_list = []
        for i in range(T):
            num1, num = input().split()
            num2, num3 = num.split("=")
            ex = []
            ex.append(int(num1))
            ex.append(int(num2))
            ex.append(int(num3))
            if ex[0]+ex[1] == ex[2]:
                sign_list.append("+")
            elif ex[0]-ex[1] == ex[2]:
                sign_list.append("-")
            elif ex[0]*ex[1] == ex[2]:
                sign_list.append("*")
            else:
                sign_list.append("I")
        name_list = []
        for i in range(T):
            N, E, R = input().split()
            E = int(E)
            if sign_list[E-1] != R:
                name_list.append(N)

        if len(name_list) == 0:
            print("You Shall All Pass!")
        elif len(name_list) == T:
            print("None Shall Pass!")
        else:
            name_list.sort()
            print(*name_list)
    except EOFError:
        break