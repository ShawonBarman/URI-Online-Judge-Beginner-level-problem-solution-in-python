N = int(input())
total_service = 0
total_service_su = 0
total_block = 0
total_block_su = 0
total_attack = 0
total_attack_su = 0
for i in range(N):
    name = input()
    numbers_1 = list(map(int, input().split()))[:3]
    numbers_2 = list(map(int, input().split()))[:3]
    total_service += numbers_1[0]
    total_service_su += numbers_2[0]
    total_block += numbers_1[1]
    total_block_su += numbers_2[1]
    total_attack += numbers_1[2]
    total_attack_su += numbers_2[2]
print("Pontos de Saque: {:.2f} %.".format((total_service_su/total_service)*100))
print("Pontos de Bloqueio: {:.2f} %.".format((total_block_su/total_block)*100))
print("Pontos de Ataque: {:.2f} %.".format((total_attack_su/total_attack)*100))