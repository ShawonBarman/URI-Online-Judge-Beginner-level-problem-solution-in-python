import math
num = int(input())

fib = (math.pow(((1+math.sqrt(5))/2),num) - math.pow(((1-math.sqrt(5))/2),num))/math.sqrt(5)

print("{:.1f}".format(fib))