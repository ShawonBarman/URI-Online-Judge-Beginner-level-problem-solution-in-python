for i in range(7):
    for j in range(39):
        if i == 0 or i == 6:
            print('-',end="")
        if i >= 1 and i <=5:
            if j == 0:
                print('|',end='')
            elif j == 38:
                print('|',end='')
            else:
                print(' ',end='')
    print()

#Another easiest way:
# print("---------------------------------------")
# print("|                                     |")
# print("|                                     |")
# print("|                                     |")
# print("|                                     |")
# print("|                                     |")
# print("---------------------------------------")