num_list = []
num_list.append(0)
num_list.append(1)
for i in range(2,61):
    num_list.append(num_list[i-1]+num_list[i-2])
T = int(input())
for i in range(T):
    N = int(input())
    print("Fib({}) = {}".format(N,num_list[N]))