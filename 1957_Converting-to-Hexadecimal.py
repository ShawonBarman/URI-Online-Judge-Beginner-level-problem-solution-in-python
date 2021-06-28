def convert_decimal_to_hexadecimal(dec):
    hexa = ""
    while dec != 0:
        rem = dec%16
        if rem >= 0 and rem <= 9:
            hexa += str(rem)
        elif rem == 10:
            hexa += "A"
        elif rem == 11:
            hexa += "B"
        elif rem == 12:
            hexa += "C"
        elif rem == 13:
            hexa += "D"
        elif rem == 14:
            hexa += "E"
        elif rem == 15:
            hexa += "F"
        dec = int(dec/16)
    return hexa
dec = int(input())
hexa = convert_decimal_to_hexadecimal(dec)
ans = hexa[::-1]
print(ans)