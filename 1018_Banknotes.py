num = int(input())
print(num)
print("{} nota(s) de R$ 100,00".format(int(num/100)))
ans = num%100
print("{} nota(s) de R$ 50,00".format(int(ans/50)))
ans = ans%50
print("{} nota(s) de R$ 20,00".format(int(ans/20)))
ans = ans%20
print("{} nota(s) de R$ 10,00".format(int(ans/10)))
ans = ans%10
print("{} nota(s) de R$ 5,00".format(int(ans/5)))
ans = ans%5
print("{} nota(s) de R$ 2,00".format(int(ans/2)))
ans = ans%2
print("{} nota(s) de R$ 1,00".format(int(ans/1)))