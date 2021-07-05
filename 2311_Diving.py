N = int(input())
dic = {}
for i in range(N):
    name = input()
    D = float(input())
    seven_score = list(map(float, input().split()))[:7]
    highest_score = max(seven_score)
    lowest_score = min(seven_score)
    total_score = sum(seven_score) - highest_score - lowest_score
    final_score = total_score * D
    dic.update({name:final_score})
for name,score in dic.items():
    print("{} {:.2f}".format(name, score))