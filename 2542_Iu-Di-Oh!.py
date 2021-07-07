while True:
    try:
        N = int(input())
        M, L = input().split()
        marcos_deck = []
        leonardos_deck = []
        for i in range(int(M)):
            num = list(map(int, input().split()))[:N]
            marcos_deck.append(num)
        for j in range(int(L)):
            num = list(map(int, input().split()))[:N]
            leonardos_deck.append(num)
        CM, CL = input().split()
        A = int(input())
        m = marcos_deck[int(CM)-1][A-1]
        l = leonardos_deck[int(CL)-1][A-1]
        if m > l:
            print("Marcos")
        elif m < l:
            print("Leonardo")
        else:
            print("Empate")
    except EOFError:
        break