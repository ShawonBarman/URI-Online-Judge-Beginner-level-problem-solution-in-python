#p = 1 then player 1 chooses even
#p = 0 then player 1 chooses odd
#j1 represents respectively the numbers that player 1 chose
#j2 represents respectively the number that player 2 chose
#r represents if player 1 cheated
#if r = 1 then player 1 cheated
#if r = 0 then player 1 did not cheated
#a represents if player 2 accused player 1 of cheating
#if a = 1 then he/she did
#if a = 0 then he/she did not
#Print "Jogador 1 ganha!" if player 1 won
#Print "Jogador 2 ganha!" if player 2 won

p, j1, j2, r, a = input().split()
p = int(p)
j1 = int(j1)
j2 = int(j2)
r = int(r)
a = int(a)
sum = j1 + j2

if r==0 and a==1:
    print("Jogador 1 ganha!")
elif r==1 and a==0:
    print("Jogador 1 ganha!")
elif r==1 and a==1:
    print("Jogador 2 ganha!")
else:
    if p==1 and sum%2==0:
        print("Jogador 1 ganha!")
    elif p==0 and sum%2!=0:
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")