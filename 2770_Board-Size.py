while True:
    try:
        x, y, m = map(int, input().split())
        while m!= 0:
            m -= 1
            xi, yi = map(int, input().split())
            if (xi <= x and yi <= y) or (xi <= y and yi <= x):
                print("Sim")
            else:
                print("Nao")
    except EOFError:
        break