A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if A>B and B<=C:
    print(":)")
elif A<B and B>=C:
    print(":(")
elif A<B and B<C and ((B-A) > (C-B)):
    print(":(")
elif A<B and B<C and ((B-A) <= (C-B)):
    print(":)")
elif A>B and B>C and ((A-B) > (B-C)):
    print(":)")
elif A>B and B>C and ((A-B) <= (B-C)):
    print(":(")
elif A==B:
    if B<C:
        print(":)")
    else:
        print(":(")

count = 0
list_sum = []
while(True):
    list_crow = []
    while(True):
        inp = input()
        list_crow.append(inp)
        if inp == "caw caw":
            count += 1
            break
    sum = 0
    if "--*" in list_crow:
        total = list_crow.count("--*")
        sum += (total*1)
    if "*--" in list_crow:
        total = list_crow.count("*--")
        sum += (total * 4)
    list_sum.append(sum)
    if count == 3:
        break
for i in range(len(list_sum)):
    print(list_sum[i])