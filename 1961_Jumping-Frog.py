P, N = input().split()
P = int(P)
N = int(N)
arr = list(map(int,input().split()))[:N]
count = 0
for i in range(len(arr)-1):
    ans = abs(arr[i]-arr[i+1])
    if ans <= P:
        count += 1
    else:
        print("GAME OVER")
        break
if count == len(arr)-1:
    print("YOU WIN")