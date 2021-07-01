available_notes = [2,5,10,20,50,100]
while True:
    N, M = input().split()
    N = int(N)
    M = int(M)
    if N == 0 and M == 0:
        break
    back = M - N
    if back > 100:
        back -= 100
    elif back > 50:
        back -= 50
    elif back > 20:
        back -= 20
    elif back > 10:
        back -= 10
    elif back > 5:
        back -= 5
    elif back >= 2:
        back -= 2
    x = 0
    for i in range(len(available_notes)-1,-1,-1):
        if (back - available_notes[i]) == 0:
            x = 2
    if x == 2:
        print("possible")
    else:
        print("impossible")