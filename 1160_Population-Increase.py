T = int(input())
if T>=1 and T<=3000:
    for i in range(T):
        PA, PB, G1, G2 = input().split()
        PA = int(PA)
        PB = int(PB)
        G1 = float(G1)
        G2 = float(G2)
        count = 0
        while(PA<=PB):
            totalA = int((PA*(G1/100)))
            totalB = int((PB*(G2/100)))
            PA += totalA
            PB += totalB
            count += 1
            if count>100:
                print("Mais de 1 seculo.")
                break
        if count<=100:
            print("{} anos.".format(count))