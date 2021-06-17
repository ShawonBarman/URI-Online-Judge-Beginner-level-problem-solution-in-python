num = int(input())
print("{} ano(s)".format(int(num/365)))
print("{} mes(es)".format(int((num%365)/30)))
print("{} dia(s)".format(num%365%30))