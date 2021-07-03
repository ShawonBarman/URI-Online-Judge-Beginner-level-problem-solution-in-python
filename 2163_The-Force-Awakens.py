N, M = input().split()
N = int(N)
M = int(M)
num_arr = []
for i in range(N):
    new_arr = list(map(int, input().split()))[:M]
    num_arr.append(new_arr)
x = 0
y = 0
for i in range(N):
    for j in range(M):
        if num_arr[i][j] == 42 and i>0 and i+1<N and j>0 and j+1<M:
            if num_arr[i-1][j-1]==7 and num_arr[i-1][j]==7 and num_arr[i-1][j+1]==7 and num_arr[i][j-1]==7 and num_arr[i][j+1]==7 and num_arr[i+1][j-1]==7 and num_arr[i+1][j]==7 and num_arr[i+1][j+1]==7:
                x = i+1
                y = j+1

print(x,y)