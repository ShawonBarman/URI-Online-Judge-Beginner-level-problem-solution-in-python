while True:
    try:
        N = int(input())
        record = []
        count = 0
        global avg
        for i in range(N):
            T, D = input().split()
            T = int(T)
            D = int(D)
            count += 1
            if count==1:
                avg = D / T
                record.append(1)
            else:
                if D/T > avg:
                    avg = D/T
                    record.append(1)
                else:
                    record.append(0)
        for i in range(len(record)):
            if record[i] == 1:
                print(i+1)

    except EOFError:
        break