N = int(input())
for i in range(N):
    name, force = input().split()
    force = int(force)
    if name == "Thor":
        print("Y")
    else:
        print("N")