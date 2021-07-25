n = int(input())
while n != 0:
    n -= 1
    inp = input()
    if inp == "P=NP":
        print("skipped")
    else:
        a, b = inp.split("+")
        print(int(a)+int(b))

# n = int(input())
# count = 0
# while n != 0:
#     n -= 1
#     hero = input()
#     if "COD" in hero:
#         continue
#     else:
#         count += 1
# print(count)