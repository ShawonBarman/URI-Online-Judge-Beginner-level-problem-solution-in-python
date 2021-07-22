n = int(input())
char = input()
while n != 0:
    n -= 1
    pos = int(input())
    if (pos == 1 and char == "A"):
        char = "B"
    elif (pos == 1 and char == "B"):
        char = "A"
    elif (pos == 2 and char == "B"):
        char = "C"
    elif (pos == 2 and char == "C"):
        char = "B"
    elif (pos == 3 and char == "C"):
        char = "A"
    elif (pos == 3 and char == "A"):
        char = "C"
print(char)