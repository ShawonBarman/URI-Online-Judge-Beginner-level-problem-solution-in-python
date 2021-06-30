S, T, F = input().split()
S = int(S)
T = int(T)
F = int(F)
global ans
if S <= 12 :
    ans = S + T + F
else:
    ans = S + T + F
if ans > 24:
    print(ans-24)
elif ans < 0:
    print(ans+24)
else:
    print(ans)