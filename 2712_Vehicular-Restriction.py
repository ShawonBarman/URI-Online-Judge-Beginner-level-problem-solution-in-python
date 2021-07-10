n = int(input())
for i in range(n):
    inp = input()
    if len(inp) != 8 or inp[3] != '-':
        print("FAILURE")
    else:
        char, digit = inp.split('-')
        # print(char, digit)
        # print(char[2], digit[3])
        count_alpha = 0
        count_digit = 0
        for i in range(len(char)):
            if char.isalpha() and char.isupper():
                count_alpha += 1
        for i in range(len(digit)):
            if digit[i].isdigit():
                count_digit += 1
        if count_alpha == 3 and count_digit == 4:
            if digit[3] == '1' or digit[3] == '2':
                print("MONDAY")
            elif digit[3] == '3' or digit[3] == '4':
                print("TUESDAY")
            elif digit[3] == '5' or digit[3] == '6':
                print("WEDNESDAY")
            elif digit[3] == '7' or digit[3] == '8':
                print("THURSDAY")
            elif digit[3] == '9' or digit[3] == '0':
                print("FRIDAY")
        else:
            print("FAILURE")