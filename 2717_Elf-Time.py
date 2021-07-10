n = int(input())
a, b = map(int, input().split())
dif = n - (a + b)
if dif >= 0:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")