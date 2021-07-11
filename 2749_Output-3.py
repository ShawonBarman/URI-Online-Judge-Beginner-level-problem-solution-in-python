for i in range(7):
    for j in range(39):
        if i == 0 or i == 6:
            print('-',end="")
        if i >= 1 and i <=5:
            if j == 0:
                print('|',end='')
            elif j == 38:
                print('|',end='')
            elif i == 1 and j == 1:
                print("x",end='')
            elif i == 1 and j == 3 :
                print("=",end='')
            elif i == 1 and j == 5:
                print("3",end='')
            elif i == 1 and j == 6:
                print("5",end='')
            elif i == 3 and j == 16:
                print("x",end='')
            elif i == 3 and j == 18:
                print("=",end='')
            elif i == 3 and j == 20:
                print("3",end='')
            elif i == 3 and j == 21:
                print("5",end='')
            elif i == 5 and j == 32:
                print("x",end='')
            elif i == 5 and j == 34:
                print("=",end='')
            elif i == 5 and j == 36:
                print("3",end='')
            elif i == 5 and j == 37:
                print("5",end='')
            else:
                print(' ',end='')
    print()

#Another easiest way:
# print("---------------------------------------")
# print("|x = 35                               |")
# print("|                                     |")
# print("|                x = 35               |")
# print("|                                     |")
# print("|                               x = 35|")
# print("---------------------------------------")