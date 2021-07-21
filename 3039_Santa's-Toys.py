n = int(input())
boy = 0
girl = 0
while n != 0:
    n -= 1
    name, gender = input().split()
    if gender == "M":
        boy += 1
    elif gender == "F":
        girl += 1
print(boy,"carrinhos")
print(girl,"bonecas")