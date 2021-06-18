salary = float(input())
if salary>=0 and salary<=400:
    print("Novo salario: {0:.2f}".format(salary+(salary*(15/100))))
    print("Reajuste ganho: {0:.2f}".format(salary*(15/100)))
    print("Em percentual: {} %".format(15))
elif salary>=400.01 and salary<=800:
    print("Novo salario: {0:.2f}".format(salary + (salary * (12 / 100))))
    print("Reajuste ganho: {0:.2f}".format(salary * (12 / 100)))
    print("Em percentual: {} %".format(12))
elif salary>=800.01 and salary<=1200:
    print("Novo salario: {0:.2f}".format(salary + (salary * (10 / 100))))
    print("Reajuste ganho: {0:.2f}".format(salary * (10 / 100)))
    print("Em percentual: {} %".format(10))
elif salary>=1200.01 and salary<=2000:
    print("Novo salario: {0:.2f}".format(salary + (salary * (7 / 100))))
    print("Reajuste ganho: {0:.2f}".format(salary * (7 / 100)))
    print("Em percentual: {} %".format(7))
else:
    print("Novo salario: {0:.2f}".format(salary + (salary * (4 / 100))))
    print("Reajuste ganho: {0:.2f}".format(salary * (4 / 100)))
    print("Em percentual: {} %".format(4))