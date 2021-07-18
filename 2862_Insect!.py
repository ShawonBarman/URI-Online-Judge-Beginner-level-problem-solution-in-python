n = int(input())
while n != 0:
    n -= 1
    inp = int(input())
    if inp <= 8000:
        print("Inseto!")
    else:
        print("Mais de 8000!")