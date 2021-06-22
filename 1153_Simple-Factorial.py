def factorial(num):
    if num <= 0:
        return 1
    return num*factorial(num-1)
N = int(input())
if N>0 and N<13:
    print(factorial(N))