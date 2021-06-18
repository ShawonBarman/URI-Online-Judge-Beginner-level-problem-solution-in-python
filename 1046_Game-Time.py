start_time, end_time = input().split()
ans = 0
if int(start_time)>12 or int(end_time)<12:
    ans = (24-int(start_time))+int(end_time)
else:
    ans = int(end_time)-int(start_time)
print("O JOGO DUROU {} HORA(S)".format(ans))