#pedra=rock, papel=paper, tesoura=scissors, lagart=lizard, spock=spock
T = int(input())
if T <= 100:
    for i in range(1,T+1):
        sheldon, raj = input().split()
        if sheldon == raj:
            print("Caso #{}: De novo!".format(i))
        elif (sheldon=="tesoura" and raj=="papel") or (sheldon=="papel" and raj=="pedra") or \
            (sheldon == "pedra" and raj == "lagarto") or (sheldon == "lagarto" and raj == "Spock") \
            or (sheldon == "Spock" and raj == "tesoura") or (sheldon == "tesoura" and raj == "lagarto") \
            or (sheldon == "lagarto" and raj == "papel") or (sheldon == "papel" and raj == "Spock") \
            or (sheldon == "Spock" and raj == "pedra") or (sheldon == "pedra" and raj == "tesoura"):
            print("Caso #{}: Bazinga!".format(i))
        else:
            print("Caso #{}: Raj trapaceou!".format(i))