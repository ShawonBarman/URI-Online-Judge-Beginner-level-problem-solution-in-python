while True:
    try:
        t = int(input())
        mini = 9999.0
        for i in range(t):
            num = float(input())
            if num < mini:
                mini = num
        print(mini)
    except EOFError:
        break