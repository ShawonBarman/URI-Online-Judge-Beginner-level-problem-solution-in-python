while True:
    try:
        num = int(input())
        if num>=1001 and num<=9999:
            password = num - 1
            print(password)
    except EOFError:
        break