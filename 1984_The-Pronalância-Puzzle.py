num = input()
inverted_num = num[::-1]
if inverted_num[0] == "0":
    print("0{}".format(int(inverted_num)))
else:
    print("{}".format(int(inverted_num)))