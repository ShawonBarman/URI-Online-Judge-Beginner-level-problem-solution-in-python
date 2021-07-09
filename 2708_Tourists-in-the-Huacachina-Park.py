sum = 0
count = 0
while True:
    inp = input()
    if inp == "ABEND":
        break
    inp = inp.split()
    if inp[0] == "SALIDA":
        count += 1
        sum += int(inp[1])
    elif inp[0] == "VUELTA":
        count -= 1
        sum -= int(inp[1])
print(sum)
print(count)
