A = []
for i in range(100):
    num = input()
    num = float(num)
    A.append(num)
for i in  range(len(A)):
    if A[i] <= 10:
        print("A[{}] = {:.1f}".format(i, A[i]))