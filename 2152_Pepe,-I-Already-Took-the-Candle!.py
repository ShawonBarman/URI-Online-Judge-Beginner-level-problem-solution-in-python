num = int(input())
for i in range(num):
    H, M, O = input().split()
    if len(H) < 2:
        H = '0' + H
    if len(M) < 2:
        M = '0' + M
    t = H + ":" + M
    if int(O) == 1:
        print(t,"- A porta abriu!")
    elif int(O) == 0:
        print(t,"- A porta fechou!")