while True:
    T = int(input())
    if T == 0:
        break
    else:
        sum = 0
        for i in range(T):
            inp = input().split()
            amount = int(inp[0])
            name = ' '.join(inp[1:])
            if name == "suco de laranja":
                sum += (120 * amount)
            elif name == "morango fresco":
                sum += (85 * amount)
            elif name == "mamao":
                sum += (85 * amount)
            elif name == "goiaba vermelha":
                sum += (70 * amount)
            elif name == "manga":
                sum += (56 * amount)
            elif name == "laranja":
                sum += (50 * amount)
            elif name == "brocolis":
                sum += (34 * amount)

        if sum < 110:
            print("Mais {} mg".format(110 - sum))
        elif sum > 130:
            print("Menos {} mg".format(sum-130))
        else:
            print("{} mg".format(sum))