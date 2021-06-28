from decimal import Decimal
num = input()
if num[0] != '-':
    print("+",end="")
print("%.4E" %Decimal(num))