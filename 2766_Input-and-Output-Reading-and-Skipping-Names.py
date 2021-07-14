arr = []
for i in range(1,11):
    name = input()
    if i == 3 or i == 7 or i == 9:
        arr.append(name)
for i in arr:
    print(i)