in_win = 0
gr_win = 0
draw = 0
grenais = 0
while(True):
    inter, gremio = input().split()
    inter = int(inter)
    gremio = int(gremio)
    grenais+=1
    if inter>gremio:
        in_win+=1
    if inter<gremio:
        gr_win+=1
    if inter==gr_win:
        draw+=1
    print("Novo grenal (1-sim 2-nao)")
    num = int(input())
    if num==1:
        continue
    if num == 2:
        break
print("{} grenais".format(grenais))
print("Inter:{}".format(in_win))
print("Gremio:{}".format(gr_win))
print("Empates:{}".format(draw))
if in_win==gr_win:
    print("Não houve vencedor")
elif in_win>gr_win:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")