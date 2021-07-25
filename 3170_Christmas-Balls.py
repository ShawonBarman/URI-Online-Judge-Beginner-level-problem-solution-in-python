b = int(input())
g = int(input())
b = round(g/2)-b
if b > 0:
    print("Faltam {} bolinha(s)".format(b))
else:
    print("Amelia tem todas bolinhas!")