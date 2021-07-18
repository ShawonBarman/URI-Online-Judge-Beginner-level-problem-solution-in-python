while True:
    try:
        inp = input()
        if inp == "direita":
            print("frances")
        elif inp == "esquerda":
            print("ingles")
        elif inp == "nenhuma":
            print("portugues")
        elif inp == "as duas":
            print("caiu")
    except EOFError:
        break