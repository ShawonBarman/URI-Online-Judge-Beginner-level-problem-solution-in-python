def mini(a, b):
	if a < b:
		return a
	else:
		return b
def calculate(l, c, matrix, memo):
	sum = 0
	if memo[l][c] != 0:
		return memo[l][c]
	if l == 1:
		memo[l][c] = matrix[l][c]
		return memo[l][c]
	for i in range(l):
		c += 1
		sum += matrix[l][c]
	memo[l][c] = sum + mini(calculate(l-1, c, matrix, memo), calculate(l-1, c+1, matrix, memo))
	return memo[l][c]

n = int(input())
arr = []
memo = []
for i in range(n):
	arr.append(list(map(int, input().split()))[:n])
for i in range(n):
	new_arr = []
	for j in range(n):
		new_arr.append(-1)
	memo.append(new_arr)
print(calculate(n, 1, arr, memo))

#something was wrong. right solution will come in future