while True:
    try:
        inp = input()
        sum = 0
        if len(inp) == 1:
            sum += (ord(inp[0]) - ord("A") + 1) * 1
        elif len(inp) == 2:
            sum += (ord(inp[1]) - ord("A") + 1) * 1 + (ord(inp[0]) - ord("A") + 1) * 26
        elif len(inp) == 3:
            sum = sum + (ord(inp[2]) - ord("A") + 1) * 1 + (ord(inp[1]) - ord("A") + 1) * 26 + (ord(inp[0]) - ord("A") + 1) * (26 * 26)

        if sum >= 1 and sum <= 16384:
            print(sum)
        else:
            print("Essa coluna nao existe Tobias!")
    except EOFError:
        break