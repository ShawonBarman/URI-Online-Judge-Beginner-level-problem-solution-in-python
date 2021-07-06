T = int(input())
for i in range(T):
    word = input()
    if len(word) > 0 and len(word) <= 25:
        print("Y")
    else:
        print("N")