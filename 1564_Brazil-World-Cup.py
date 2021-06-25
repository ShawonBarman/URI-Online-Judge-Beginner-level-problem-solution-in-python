while(True):
    try:
        num = int(input())
        if num >=0 and num <= 100:
            if num==0:
                print("vai ter copa!")
            else:
                print("vai ter duas!")
    except EOFError:
        break