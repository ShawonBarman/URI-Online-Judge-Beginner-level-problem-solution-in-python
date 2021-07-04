A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if A-B == 0 or A-C == 0 or B-C == 0 or A+B+C == 0 or A+B-C == 0 or A-B+C == 0 or A-B-C == 0:
    print("S")
else:
    print("N")