salary = float(input())
if salary>=0 and salary<=2000:
    print("Isento")
elif salary>=2000.01 and salary<=3000:
    x = salary-2000
    print("R$ {0:.2f}".format(x*(8/100)))
elif salary>=3000.01 and salary<=4500:
    x = salary - 2000
    print("R$ {0:.2f}".format((1000*(8/100))+((x-1000)*(18/100))))
elif salary>4500:
    x = salary - 2000
    print("R$ {0:.2f}".format((1000*(8/100))+(1500*(18/100))+((x-2500)*(28/100))))