T = int(input())
for i in range(T):
    B = int(input())
    dabriel = list(map(int, input().split()))[:3]
    guarte = list(map(int, input().split()))[:3]
    value_d = ((dabriel[0]+dabriel[1])/2)
    value_g = ((guarte[0]+guarte[1])/2)
    if dabriel[2]%2==0:
        value_d += B
    if guarte[2]%2==0:
        value_g += B
    if value_d > value_g:
        print("Dabriel")
    elif value_d < value_g:
        print("Guarte")
    else:
        print('Empate')