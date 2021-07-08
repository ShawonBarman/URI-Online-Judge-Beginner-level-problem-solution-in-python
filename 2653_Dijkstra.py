mySet = set()
while True:
    try:
        char = input()
    except EOFError:
        break
    mySet.add(char)
    if char == '(' or char == ')':
        break
print(len(mySet))