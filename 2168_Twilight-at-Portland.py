N = int(input())
cameras_list = []
for i in range(N+1):
    cameras = list(map(int, input().split()))[:N+1]
    cameras_list.append(cameras)
for i in range(N):
    for j in range(N):
        if (cameras_list[i][j] + cameras_list[i][j+1] + cameras_list[i+1][j] + cameras_list[i+1][j+1]) < 2:
            print("U", end="")
        else:
            print("S", end="")
    print()