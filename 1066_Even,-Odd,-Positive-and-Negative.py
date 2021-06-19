even_num = 0
odd_num = 0
positive_num = 0
negative_num = 0
for i in range(5):
    num = int(input())
    if num%2==0:
        even_num+=1
    if num%2!=0:
        odd_num+=1
    if num>0:
        positive_num+=1
    if num<0:
        negative_num+=1
print("{} valor(es) par(es)".format(even_num))
print("{} valor(es) impar(es)".format(odd_num))
print("{} valor(es) positivo(s)".format(positive_num))
print("{} valor(es) negativo(s)".format(negative_num))