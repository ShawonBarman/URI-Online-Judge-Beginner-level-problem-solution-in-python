n = int(input())
while n != 0:
    n -= 1
    num_list = list(map(int, input().split()))
    ans = (sum(num_list) + 1) - (num_list[0] * 2)
    print(ans)