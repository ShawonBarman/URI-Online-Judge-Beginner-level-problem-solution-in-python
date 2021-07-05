A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if A+B<=C or A+C<=B or B+C<=A:
    print("Invalido")
else:
    if A==B and B==C:
        print("Valido-Equilatero")
    elif A==B or A==C or B==C:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    if A*A == (B*B)+(C*C) or B*B == (A*A)+(C*C) or C*C == (A*A)+(B*B):
        print("Retangulo: S")
    else:
        print("Retangulo: N")