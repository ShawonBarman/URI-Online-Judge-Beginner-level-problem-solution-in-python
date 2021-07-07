while True:
    try:
        N, mini, maxi = input().split()
        count = 0
        for i in range(int(N)):
            num = int(input())
            if num >= int(mini) and num <= int(maxi):
                count += 1
        print(count)
    except EOFError:
        break