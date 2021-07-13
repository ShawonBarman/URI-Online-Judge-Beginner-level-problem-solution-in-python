num = input()
x, y = num.split(".")
num = y + "." + x
if num[0]=='0':
    num = num[1:]
print(num)