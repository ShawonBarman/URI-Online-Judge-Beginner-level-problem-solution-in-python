while True:
    try:
        word = input().upper()
        N = int(input())
        numbers = list(map(int, input().split()))[:N]
        ans = ""
        for i in numbers:
            ans += word[i-1]
        print(ans)
    except EOFError:
        break