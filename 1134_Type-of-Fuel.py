alcohol = 0
gasoline = 0
diesel = 0
while(True):
    num = int(input())
    if num == 1:
        alcohol+=1
    elif num == 2:
        gasoline+=1
    elif num == 3:
        diesel+=1
    elif num == 4:
        break
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool:",alcohol)
print("Gasolina:",gasoline)
print("Diesel:",diesel)