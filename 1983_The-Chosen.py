num = int(input())
dic = {}
for i in range(num):
    reg_num, note = input().split()
    reg_num = int(reg_num)
    note = float(note)
    dic.update({reg_num:note})
max = -999999
reg_num = 0
for x in dic.keys():
    if dic[x] > max:
        reg_num = x
        max = dic[x]
if max < 8:
    print("Minimum note not reached")
else:
    print(reg_num)