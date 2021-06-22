list_fib = []
list_fib.append(0)
list_fib.append(1)
N = int(input())
for i in range(N-1):
    if i<=1:
        print(list_fib[i],end=" ")
    else:
        list_fib.append(list_fib[i-1]+list_fib[i-2])
        print(list_fib[i],end=" ")
print(list_fib[N-2]+list_fib[N-3])
