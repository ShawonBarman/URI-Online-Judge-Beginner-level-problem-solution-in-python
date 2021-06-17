import  math
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maiorAB = (a+b+abs(a-b))/2
greatest_number = (int(maiorAB)+c+abs(maiorAB-c))/2
print("{} eh o maior".format(int(greatest_number)))