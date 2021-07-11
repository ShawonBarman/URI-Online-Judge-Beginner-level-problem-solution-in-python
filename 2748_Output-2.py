for i in range(7):
    for j in range(39):
        if i == 0 or i == 6:
            print('-',end="")
        if i >= 1 and i <=5:
            if j == 0:
                print('|',end='')
            elif j == 38:
                print('|',end='')
            elif i == 1 and j == 9:
                print("R",end='')
            elif i == 1 and j == 10:
                print("o",end='')
            elif i == 1 and j == 11:
                print("b",end='')
            elif i == 1 and j == 12:
                print("e",end='')
            elif i == 1 and j == 13:
                print("r",end='')
            elif i == 1 and j == 14:
                print("t",end='')
            elif i == 1 and j == 15:
                print("o",end='')
            elif i == 3 and j == 9:
                print("5",end='')
            elif i == 3 and j == 10:
                print("7",end='')
            elif i == 3 and j == 11:
                print("8",end='')
            elif i == 3 and j == 12:
                print("6",end='')
            elif i == 5 and j == 9:
                print("U",end='')
            elif i == 5 and j == 10:
                print("N",end='')
            elif i == 5 and j == 11:
                print("I",end='')
            elif i == 5 and j == 12:
                print("F",end='')
            elif i == 5 and j == 13:
                print("E",end='')
            elif i == 5 and j == 14:
                print("I",end='')
            else:
                print(' ',end='')
    print()

#Another easiest way:
# print("---------------------------------------")
# print("|        Roberto                      |")
# print("|                                     |")
# print("|        5786                         |")
# print("|                                     |")
# print("|        UNIFEI                       |")
# print("---------------------------------------")