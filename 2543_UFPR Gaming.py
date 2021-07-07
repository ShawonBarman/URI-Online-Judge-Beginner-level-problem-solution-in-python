while True:
    try:
        N, I = input().split()
        count_contra = 0
        for i in range(int(N)):
            x, y = input().split()
            if int(x) == int(I) and int(y) == 0:
                count_contra += 1
        print(count_contra)
    except EOFError:
        break