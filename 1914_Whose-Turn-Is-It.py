QT = int(input())
for i in range(QT):
    player1, choice1, player2, choice2 = input().split()
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    sum = num1+num2
    if sum%2==0:
        if choice1 == "PAR":
            print(player1)
        else:
            print(player2)
    else:
        if choice1 == "IMPAR":
            print(player1)
        else:
            print(player2)