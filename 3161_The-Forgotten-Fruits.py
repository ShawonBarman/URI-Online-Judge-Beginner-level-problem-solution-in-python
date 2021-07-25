n, m = map(int, input().split())
for i in range(m):
    name = input()
    if i < 3:
        print("Sheldon come a fruta {}".format(name))
    if i >= 3 and i < 6:
        print("Sheldon detesta a fruta {}".format(name))

    # 15% wrong answer. correct solution will come in future