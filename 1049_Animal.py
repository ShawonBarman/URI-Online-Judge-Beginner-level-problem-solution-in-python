x = input()
y = input()
z = input()
if x == "vertebrado":
    if y == "ave":
        if z == "carnivoro":
            print("aguia")
        if z == "onivoro":
            print("pomba")
    if y == "mamifero":
        if z == "onivoro":
            print("homem")
        if z == "herbivoro":
            print("vaca")
if x == "invertebrado":
    if y == "inseto":
        if z == "hematofago":
            print("pulga")
        if z == "herbivoro":
            print("lagarta")
    if y == "anelideo":
        if z == "hematofago":
            print("sanguessuga")
        if z == "onivoro":
            print("minhoca")