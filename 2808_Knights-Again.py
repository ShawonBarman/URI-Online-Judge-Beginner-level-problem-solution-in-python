initial_position, target_position = input().split()
col1 = initial_position[0]
row1 = int(initial_position[1])
col2 = target_position[0]
row2 = int(target_position[1])
if (row1-2 == row2 or row1+2 == row2) and (chr(ord(col1)+1) == col2 or chr(ord(col1)-1) == col2):
    print("VALIDO")
elif (chr(ord(col1)+2) == col2 or chr(ord(col1)-2) == col2) and (row1-1 == row2 or row1+1 == row2):
    print("VALIDO")
else:
    print("INVALIDO")