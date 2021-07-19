e, d = map(int, input().split())
if d < e:
    print("Eu odeio a professora!")
elif d-e >= 3:
    print("Muito bem! Apresenta antes do Natal!")
elif d-e <= 1:
    print("Parece o trabalho do meu filho!")

if d+2 > 24:
    print("Fail! Entao eh nataaaaal!")
elif d+2 == 24:
    print("TCC Apresentado!")