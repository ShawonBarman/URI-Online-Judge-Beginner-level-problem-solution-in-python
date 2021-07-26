import math
def calculate(k, curMin, curMax, curCuts):
    if k == n:
        return curCuts
    absMax = curMin / t
    absMin = curMax * t
    low = math.ceil(w[k] / absMax)
    high = int(w[k] / absMin)
    # print(low,high)
    if k == 0:
        low = 1
        high = w[0]
        # print(low, high)
    for i in range(low, high+1):
        newL = w[k] / i
        # print("newL =",newL)
        if k == 0:
            curMin = curMax = newL
            # print("curMin =",curMin)

        ans = calculate(k+1, min(curMin, newL), max(curMax, newL), curCuts+i-1)
        # print("ans =",ans)
        if ans != -1:
            return ans
    return -1
t, n = input().split()
t = float(t)
n = int(n)
w = list(map(int, input().split()))[:n]
w.sort()
ans = calculate(0, w[0], w[0], 0)
print(ans)