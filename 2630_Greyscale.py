T = int(input())
case = 0
for i in range(T):
    op = input()
    R, G, B = map(int, input().split())
    case += 1
    if op == "min":
        print("Caso #{}: {}".format(case, min(R,G,B)))
    elif op == "max":
        print("Caso #{}: {}".format(case, max(R, G, B)))
    elif op == "eye":
        p = (0.30 * R) + (0.59 * G) + (0.11 * B)
        print("Caso #{}: {}".format(case, int(p)))
    else:
        print("Caso #{}: {}".format(case, int((R+G+B)/3)))