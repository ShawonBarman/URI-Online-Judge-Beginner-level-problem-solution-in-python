Ca, Ba, Aa = map(int, input().split())
Cr, Br, Ar = map(int, input().split())
sum = 0
if Ca - Cr < 0 :
    sum += (Cr - Ca)
if Ba - Br < 0 :
    sum += (Br - Ba)
if Aa - Ar < 0 :
    sum += (Ar - Aa)
print(sum)