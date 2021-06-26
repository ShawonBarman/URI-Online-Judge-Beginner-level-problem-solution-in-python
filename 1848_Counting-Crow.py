count = 0
while(True):
    list_crow = []
    sum = 0
    while(True):
        inp = input()
        if inp != "caw caw":
            inp = inp.replace('-','0')
            inp = inp.replace('*','1')
            sum += ((int(inp[0])*4)+(int(inp[1])*2)+(int(inp[2])*1))

        if inp == "caw caw":
            count += 1
            break
    print(sum)
    if count == 3:
        break