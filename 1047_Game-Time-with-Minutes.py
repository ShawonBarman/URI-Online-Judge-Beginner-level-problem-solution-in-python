start_hour, start_min, end_hour, end_min = input().split()
start_hour = int(start_hour)
start_min = int(start_min)
end_hour = int(end_hour)
end_min = int(end_min)
ans_hour = 0
ans_min = 0
if start_hour==end_hour and start_min==end_min:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24-start_hour+end_hour,start_min-end_min))
elif start_hour==end_hour and start_min<end_min:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(start_hour-end_hour,end_min-start_min))
elif start_hour==end_hour and start_min>end_min:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24-start_hour+end_hour-1,60-start_min+end_min))
elif start_hour<end_hour and start_min==end_min:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(end_hour-start_hour,start_min-end_min))
elif start_hour>end_hour and start_min==end_min:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24-start_hour+end_hour,start_min-end_min))
elif start_hour<end_hour and start_min<end_min:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(end_hour-start_hour,end_min-start_min))
elif start_hour<end_hour and start_min>end_min:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(end_hour-start_hour-1,60-start_min+end_min))
elif start_hour>end_hour and start_min<end_min:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24-start_hour-1+end_hour,end_min-start_min))
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(24+end_hour-start_hour-1, 60+end_min-start_min))

