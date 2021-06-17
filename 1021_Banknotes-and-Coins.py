num = float(input())
a = num
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(a/100)))
ans = a%100
print("{} nota(s) de R$ 50.00".format(int(ans/50)))
ans = ans%50
print("{} nota(s) de R$ 20.00".format(int(ans/20)))
ans = ans%20
print("{} nota(s) de R$ 10.00".format(int(ans/10)))
ans = ans%10
print("{} nota(s) de R$ 5.00".format(int(ans/5)))
ans = ans%5
print("{} nota(s) de R$ 2.00".format(int(ans/2)))
ans = ans%2
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(ans)))
b = num*100
res = b%100
print("{} moeda(s) de R$ 0.50".format(int(res/50)))
res = res%50
print("{} moeda(s) de R$ 0.25".format(int(res/25)))
res = res%25
print("{} moeda(s) de R$ 0.10".format(int(res/10)))
res = res%10
print("{} moeda(s) de R$ 0.05".format(int(res/5)))
res = res%5
print("{} moeda(s) de R$ 0.01".format(int(res/1)))