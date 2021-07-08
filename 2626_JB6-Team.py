while True:
    try:
        Dodo, Leo, Pepper = input().split()
        if (Dodo == "papel" and Leo == "pedra" and Pepper == "pedra") or (Dodo == "tesoura" and Leo == "papel" and Pepper == "papel") or (Dodo == "pedra" and Leo == "tesoura" and Pepper == "tesoura"):
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        elif (Dodo == "pedra" and Leo == "papel" and Pepper == "pedra") or (Dodo == "papel" and Leo == "tesoura" and Pepper == "papel") or (Dodo == "tesoura" and Leo == "pedra" and Pepper == "tesoura"):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif (Dodo == "pedra" and Leo == "pedra" and Pepper == "papel") or (Dodo == "papel" and Leo == "papel" and Pepper == "tesoura") or (Dodo == "tesoura" and Leo == "tesoura" and Pepper == "pedra"):
            print("Urano perdeu algo muito precioso...")
        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
    except EOFError:
        break