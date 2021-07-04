num = input()
x = num.count('1')
if x == 0:
    num += '0'
else:
    if x %2 == 0:
        num += '0'
    else:
        num += '1'
print(num)