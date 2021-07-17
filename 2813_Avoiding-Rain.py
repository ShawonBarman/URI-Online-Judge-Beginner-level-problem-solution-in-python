n = int(input())
c, e = 0, 0
arr = []
for i in range(n):
    sd, sn = input().split()
    if len(arr) == 0:
        if sd == "sol" and sn == "chuva":
            c += 0
            e += 1
        elif sd == "chuva" and sn == "sol":
            c += 1
            e += 0
        arr.append(sd)
        arr.append(sn)
    else:
        if arr[1] == "chuva" and sd == "chuva" and sn == "sol":
            c += 0
            e += 0
            arr[0] = sd
            arr[1] = sn
        elif arr[0] == "sol" and sd == "sol" and arr[1] == "chuva" and sn == "chuva":
            c += 0
            e += 1
        elif arr[0] == "chuva" and sd == "chuva" and arr[1] == "sol" and sn == "sol":
            c += 1
            e += 0
print(c,e)

#25% error