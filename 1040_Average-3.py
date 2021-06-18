a, b, c, d = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)
avg = ((a*2)+(b*3)+(c*4)+(d*1))/(2+3+4+1)
print("Media: {0:.1f}".format(avg))
if avg >= 7:
    print("Aluno aprovado.")
elif avg < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: {0:.1f}".format(e))
    new_avg = (e+avg)/2
    if new_avg >= 5:
        print("Aluno aprovado.")
        print("Media final: {0:.1f}".format(new_avg))
    else:
        print("Aluno reprovado.")
        print("Media final: {0:.1f}".format(new_avg))