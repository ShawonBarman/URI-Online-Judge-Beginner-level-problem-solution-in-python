#ataque = Airstrike, pedra = Rock, papel = Paper

N = int(input())
for i in range(N):
    player1 = input()
    player2 = input()
    if player1=="papel" and player2=="papel":
        print("Ambos venceram")
    elif player1=="pedra" and player2=="pedra":
        print("Sem ganhador")
    elif player1=="ataque" and player2=="ataque":
        print("Aniquilacao mutua")
    elif (player1=="ataque" and player2=="pedra") or (player1=="pedra" and player2=="papel") or (player1=="ataque" and player2=="papel"):
        print("Jogador 1 venceu")
    else:
        print("Jogador 2 venceu")