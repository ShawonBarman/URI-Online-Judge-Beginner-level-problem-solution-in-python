A = int(input())
B = int(input())
C = int(input())
arr = []
arr.append((B*2)+(C*4))
arr.append((A*2)+(C*2))
arr.append((B*2)+(A*4))
arr.sort()
print(arr[0])