while True:
    try:
        N = int(input())
        v = list(map(int, input().split()))[:N]
        ones = v.count(1)
        if (ones/N) >= (2/3):
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break