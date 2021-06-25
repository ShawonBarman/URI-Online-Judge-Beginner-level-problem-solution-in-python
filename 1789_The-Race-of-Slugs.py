while True:
    try:
        L = int(input())
        slugs = list(map(int, input().split()))[:L]
        lv = list()
        for i in range(len(slugs)):
            if slugs[i] >= 20:
                #level3
                lv.append(3)
            elif slugs[i] >= 10 and slugs[i] < 20:
                #level2
                lv.append(2)
            else:
                #level1
                lv.append(1)
        print(max(lv))
    except EOFError:
        break